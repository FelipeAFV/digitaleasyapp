import os

from django.http import HttpResponse
from django.shortcuts import render
import traceback
import datetime
import pytz
from transbank.common.integration_type import IntegrationType
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from api.permissions import ClientPermission
from django.http import HttpResponseRedirect
from django.shortcuts import render

from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions, IntegrationCommerceCodes
from transbank.webpay.webpay_plus.transaction import IntegrationApiKeys
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from auth.models import User
from clients.models import Client
import shortuuid
from .models import Service, ServiceOrders, CustomService


@api_view(['POST'])
@permission_classes([IsAuthenticated, ClientPermission])
def createTransaction(request: Request):

    # get client from request
    user: User = request.user
    client = Client.objects.get(user_id=user.id)

    if os.environ.get('ENV') == 'prod':
        return_url = reverse(viewname='createTx', request=request).replace('http','https') + 'commit'
    else:
        return_url = reverse(viewname='createTx', request=request) + 'commit'
    print(return_url)

    # Transaction creation with Transbankcredentials
    tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY, IntegrationType.TEST))

    ## DEFINING TRANSACTION PARAMETERS

    # Unique code for buying order/ service order
    buy_order = shortuuid.ShortUUID().random(length=26)

    # session id defined by a jwt in the auth system
    session_id = 'session_id'

    # TODO: obtener parametros de compra en el request

    service_id = request.data['service_id']

    # service instance
    service = ''
    try:
        service = Service.objects.get(id=service_id)
    except Service.DoesNotExist:
        return Response('No existe el servicio seleccionado', status=400)


    ammount = service.value


    # request v??lido

    santiago_tz = pytz.timezone('America/Santiago')

    # Creacion de orden de compra

    order = ServiceOrders(order_number=buy_order, session_token=session_id, ammount= ammount,
                          service=service, client=client,
                          request_date=datetime.datetime.now(tz=santiago_tz), status=ServiceOrders.NO_PROCESADO)
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
    santiago_tz = pytz.timezone('America/Santiago')
    if request.method == 'POST':
        print('Transacction status ', tx.status(request.data['TBK_TOKEN']))
    # handle success transaction
    elif request.method == 'GET':
        token_for_commit = request.query_params.get(('token_ws'))
        print('On get transaction status ', tx.status(token_for_commit))
        res = tx.commit(token_for_commit)
        res = dict(res)

        # handle errors on transaction
        if res['status'] == 'FAILED':
            return render(request=request, template_name='paymentResponse.html', context={'message': 'La transaccion ha fallado'})
        else:
            try:
                order_to_update = ServiceOrders.objects.get(tx_token=token_for_commit)
                order_to_update.status = ServiceOrders.ACTIVO
                order_to_update.first_purchase_date = datetime.datetime.now(tz=santiago_tz)
                order_to_update.last_purchase_date = datetime.datetime.now(tz=santiago_tz)
                expiration_date = datetime.datetime.now(tz=santiago_tz)
                expiration_date = expiration_date.replace(year=expiration_date.year+1)
                order_to_update.expiration_date = expiration_date
                order_to_update.save()
            except Service.DoesNotExist:
                return render(request=request, template_name='paymentResponse.html', context={'message': 'Error: servicio no encontrado'})
            except Exception:
                return render(request=request, template_name='paymentResponse.html', context={'message': 'Error'})
            return render(request=request, template_name='paymentResponse.html', context={'message': 'Transaccion exitosa'})
    return render(request=request, template_name='paymentResponse.html', context={'message': 'Ha ocurrido un error'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def payForCustomService(request):
    token = request.data['service_token']
    try:
        custom_service: CustomService = CustomService.objects.get(token=token)
        # get client from request
        user: User = request.user

        client = Client.objects.get(user_id=user.id)
        print(client.fullname)
        if os.environ.get('ENV') == 'prod':
            return_url = reverse(viewname='createTx', request=request).replace('http', 'https') + 'commit'
        else:
            return_url = reverse(viewname='createTx', request=request) + 'commit'
        print(return_url)

        tx = Transaction(
            WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY, IntegrationType.TEST))
        # codigo unico de orden de compra
        buy_order = shortuuid.ShortUUID().random(length=26)

        # session id defined by a jwt in the auth system
        session_id = 'session_id'

        # TODO: obtener parametros de compra en el request



        ammount = custom_service.value

        # request v??lido

        santiago_tz = pytz.timezone('America/Santiago')

        # Creacion de orden de compra

        order = ServiceOrders(order_number=buy_order, session_token=session_id, ammount=ammount,
                              date=datetime.datetime.now(tz=santiago_tz), custom_service=custom_service, client=client,
                              status=ServiceOrders.NO_PROCESADO)
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

    except CustomService.DoesNotExist:
        return Response(status=400, data='Invalid token')
