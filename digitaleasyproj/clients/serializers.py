from rest_framework import serializers
from api.models import User
from .models import Client, Business
from payments.models import ServiceOrders


class BusinessSerializer(serializers.ModelSerializer):

    business_name = serializers.CharField(source='name')

    class Meta:
        model = Business
        fields = ['business_name', 'ig_account', 'goals']



class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['fullname', 'phone_number', 'email']

class UserSerializer(serializers.ModelSerializer):


    class Meta:

        model = User
        fields = [
            'username',
            'password'
        ]

class ServiceOrderSerializer(serializers.ModelSerializer):

    service = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = ServiceOrders
        fields = ['order_number','ammount','date','service']
    def get_service(self, obj: ServiceOrders):
        return obj.service.name
