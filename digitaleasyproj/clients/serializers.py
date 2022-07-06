from rest_framework import serializers
from api.models import User
from .models import Client, Business

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