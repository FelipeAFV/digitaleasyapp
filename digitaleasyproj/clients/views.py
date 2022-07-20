import traceback

from django.shortcuts import render
from payments.models import Client, ServiceOrders, Service
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from api.permissions import ClientPermission
from .serializers import UserSerializer, BusinessSerializer, ClientSerializer
from auth.models import User
from payments.serializers import ServiceSerializer
from .serializers import ServiceOrderSerializer

# Create your views here.

@api_view(['POST'])
def registerNewClient(request):

    user_serializer = UserSerializer(data=request.data)
    client_serialized = ClientSerializer(data=request.data)
    business_serialized = BusinessSerializer(data=request.data)

    # check for valid serialization
    if not client_serialized.is_valid(raise_exception=True) or not business_serialized.is_valid(raise_exception=True):
        return Response('Datos incorrectos', status=400)

    user_created: User = ''
    if user_serializer.is_valid(raise_exception=True):
        # save user to database
        user_created = user_serializer.save()
        #update to hashed pass
        user_created.role = User.CLIENT
        user_created.set_password(request.data['password'])
        user_created.save()

    ## Handle creation of client entity on success signup
    try:
        client_serialized.user = user_created
        client_created = client_serialized.save(user=user_created)
        print(client_created)

        business_serialized.save(client=client_created)
    except:
        # delete user on failure
        traceback.print_exc()
        user_created.delete()
        return Response({
            'message': 'Erron on client creation',
            'user_deleted': UserSerializer(user_created).data
        }, status=400)

    return Response('Client created', status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated, ClientPermission])
def getAllActiveServicesFromClient(request):

    client = Client.objects.get(user_id=request.user.id)

    services = ServiceOrders.objects.filter(
        client_id=client.id)
    print(services[0].service.name)
    services_serialized = ServiceOrderSerializer(services, many=True)
    print(services_serialized)
    print(type(services_serialized))
    return Response(status=200, data={
        'services': services_serialized.data
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated, ClientPermission])
def getAllAvailableServices(request):

    services = Service.objects.all()
    services_serialized = ServiceSerializer(services, many=True)
    return Response(status=200, data=services_serialized.data)
