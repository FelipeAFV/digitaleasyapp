from django.db import models
# Create your models here.
from digitaleasyproj import settings
from clients.models import Client, Business

class Service(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    value = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    description = models.TextField(max_length=150)

    class Meta:
        db_table = 'services'

class CustomService(models.Model):

    token = models.CharField(max_length=40, blank=False, null=False, unique=True)
    name = models.CharField(max_length=30, blank=False, null= False)
    description = models.CharField(max_length=150, blank=False, null= False)
    value = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)

    class Meta:
        db_table = 'custom_service'

class ServiceOrders(models.Model):

    order_number = models.CharField(max_length=26, blank=False, null=False)
    session_token = models.CharField(max_length=61, blank=False, null=False)
    ammount = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    date = models.DateField(blank=False, null=False)
    tx_token = models.CharField(max_length=70, blank=False, null=False)
    service = models.ForeignKey(Service, null=True, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False, blank=False, null=False)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    custom_service = models.ForeignKey(CustomService, null=True, on_delete=models.PROTECT)

    class Meta:
        db_table = 'service_orders'

