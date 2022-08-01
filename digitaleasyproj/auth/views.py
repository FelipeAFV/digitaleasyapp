from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.request import Request
from django.contrib.auth.models import AnonymousUser
from .models import User
from clients.models import Client
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def isAuth(request):
    return Response(status=200)

@api_view(['GET'])
def getRoutes(request):

    routes = [
        '/api/token',
        '/api/token/refresh'
    ]
    return Response(routes)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def isAuthenticated(request: Request):

    return JsonResponse(data= {
        'message': 'User authenticated'
    })

# api_view is a decorator for defining a handler for a rest request (API Rest)
@api_view(['GET'])
def userData(request: Request):
    user: User = request.user
    print(type(user))
    print(user.role)
    name_res = user.role
    if user.role == User.CLIENT:
        name_res = Client.objects.get(user_id=user.id).fullname

    return Response(data={
        'firstName': name_res,
        'lastName': user.last_name,
        'role': user.role
    })
