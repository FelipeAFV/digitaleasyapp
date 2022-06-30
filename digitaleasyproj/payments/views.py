from django.http import HttpResponse
from django.shortcuts import render
import traceback
import datetime
import pytz
from transbank.common.integration_type import IntegrationType
from rest_framework.reverse import reverse, reverse_lazy
from django.shortcuts import render

from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions, IntegrationCommerceCodes
from transbank.webpay.webpay_plus.transaction import IntegrationApiKeys
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import shortuuid
from .models import Service, ServiceOrders


# Create your views here.
@api_view(['POST'])
def createTransactionRest(request: Request):
    tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY, IntegrationType.TEST))
    buy_order = 'buyorder'
    session_id = 'sessionid'
    ammount = 22
    return_url = reverse(viewname='createTx', request=request) + '/commit'

    # la respuesta genera un token que debe ser usado para cuando se confirme la transaccion
    resp = tx.create(buy_order,session_id, ammount, return_url)
    return Response(resp)


@api_view(['POST', 'GET'])
def createTransaction(request: Request):
    tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY, IntegrationType.TEST))
    print(request.GET.get('service_id'))
    # codigo unico de orden de compra
    buy_order = shortuuid.ShortUUID().random(length=26)

    # session id defined by a jwt in the auth system
    session_id = request.headers.get('Authorization') or 'session_id'

    # TODO: obtener parametros de compra en el request
    service_id = request.GET.get('service_id')

    # service instance
    service = ''
    try:
        service = Service.objects.get(id=service_id)
    except Service.DoesNotExist:
        return Response('No existe el servicio seleccionado', status=400)


    ammount = service.value

    return_url = reverse(viewname='createTx', request=request) + 'commit'

    # request válido

    santiago_tz = pytz.timezone('America/Santiago')

    # Creacion de orden de compra

    order = ServiceOrders(order_number=buy_order, session_token=session_id, ammount= ammount,
                          date=datetime.datetime.now(tz=santiago_tz), service=service)
    created_order = ''
    try:
        order.save()
    except Exception:
        print(traceback.format_exc())
        return Response('Error al crear orden de compra', status=400)

    # la respuesta genera un token que debe ser usado para cuando se confirme la transaccion
    resp = tx.create(buy_order, session_id, ammount, return_url)

    order.tx_token = resp['token']
    try:
        order.save()
    except:
        return Response('Error al actualizar orden de compra', status=400)

    return Response(resp)


@api_view(['POST', 'GET'])
def commitTransaction(request):
    tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY, IntegrationType.TEST))
    buy_order = 'buyorder'
    session_id = 'sessionid'
    ammount = 22
    print('commiting transaction')
    print(request.method)
    # handle success transaction
    if request.method == 'GET':
        token_for_commit = request.query_params.get(('token_ws'))
        res = tx.commit(token_for_commit)
        print(res)
        print(type(res))
        res = dict(res)

        # handle errors on transaction
        if res['status'] == 'FAILED':
            return Response('La transaccion ha fallado', status=400)
        else:
            return Response('La transaccion ha sido exitosa', status=200)
    return Response('HA ocurrido un error')

