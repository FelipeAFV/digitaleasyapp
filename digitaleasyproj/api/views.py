from django.shortcuts import render
import os
from django.http import JsonResponse
from .models import NewClientData
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, NOT
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from .serializers import NewClientSerializer
from .permissions import ClientPermission, AdminPermission
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated, ClientPermission])
def hello(request):
    print(request.user.role)
    print(os.environ.get('MYVAR'))
    print(request.user.groups)
    return Response('Hello')



@api_view(['DELETE'])
@permission_classes([IsAuthenticated, AdminPermission])
def deleteClient(request, id):
    try:
        newClientToDelete = NewClientData.objects.get(id=int(id))
        newClientToDelete.delete()
        return Response('Client deleted')
    except Exception:

        return Response(data='Error', status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated, AdminPermission])
def listAllNewClients(request):

    clients = list(NewClientData.objects.all())

    clients_res_data = ''

    res = {
        'message': '',
        'data': ''
    }

    if len(clients) == 0:
        res['message'] = 'No hay clientes nuevos'
    else:
        clients_serializer = NewClientSerializer(clients, many=True)
        clients_res_data = clients_serializer.data
        res['data'] = clients_res_data
    return JsonResponse(res, safe=False)