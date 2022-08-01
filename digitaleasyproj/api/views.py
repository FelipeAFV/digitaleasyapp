from django.shortcuts import render
import os
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, NOT
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
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
    return Response('Client deleted')



@api_view(['POST'])
@permission_classes([IsAuthenticated, AdminPermission])
def listAllNewClients(request):


    return JsonResponse('res', safe=False)