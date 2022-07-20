from rest_framework import serializers
from .models import Service, CustomService


class ServiceSerializer(serializers.ModelSerializer):

    class Meta():

        model = Service
        fields = '__all__'

class CustomServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomService
        fields = ['name', 'value', 'description']