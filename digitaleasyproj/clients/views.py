import traceback

from django.shortcuts import render
from payments.models import Client
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth.models import User


# Create your views here.

@api_view(['POST'])
def registerNewClient(request):

    user_serializer = UserSerializer(data=request.data)
    user_created: User = ''
    if user_serializer.is_valid(raise_exception=True):
        # save user to database
        user_created = user_serializer.save()
        #update to hashed pass
        user_created.set_password(request.data['password'])
        user_created.save()

    ## Handle creation of client entity on success signup
    try:
        new_client = Client(user=user_created, client_name=request.data['client_name'])
        new_client.save()
    except:
        # delete user on failure
        traceback.print_exc()
        user_created.delete()
        return Response({
            'message': 'Erron on client creation',
            'user_deleted': UserSerializer(user_created).data
        }, status=400)

    return Response('Client created', status=200)
