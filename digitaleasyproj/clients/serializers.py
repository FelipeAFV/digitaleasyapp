from rest_framework import serializers
from auth.models import User
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

    status = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = ServiceOrders
        fields = ['id','order_number','ammount','last_purchase_date','expiration_date','service', 'status']
    def get_service(self, obj: ServiceOrders):
        return obj.service.name

    def get_status(self, obj):
        for stat in ServiceOrders.status_choices:
            if stat[0] == obj.status:
                return stat[1]

        return 'No definido'
