from rest_framework import serializers
from .models import NewClientData
class NewClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewClientData
        fields ='__all__'
