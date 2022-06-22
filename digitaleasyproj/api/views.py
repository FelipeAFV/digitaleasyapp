from django.shortcuts import render
from django.http import JsonResponse
from .models import NewClientData
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from .serializers import NewClientSerializer
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hello(request):
    print(request.user.groups)
    return Response('Hello')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def listAllNewClients(request):

    clients = list(NewClientData.objects.all())

    print('Lista de clientes',clients)
    clients_res_data = ''
    print('Data', clients_res_data)


    print(clients)
    res = {
        'message': '',
        'data': ''
    }
    print('All clients ', clients)

    if (len(clients) == 0):
        res['message'] = 'No hay clientes nuevos'
    else:
        clients_serializer = NewClientSerializer(clients, many=True)
        clients_res_data = clients_serializer.data
        res['data'] = clients_res_data
    return JsonResponse(res, safe=False)