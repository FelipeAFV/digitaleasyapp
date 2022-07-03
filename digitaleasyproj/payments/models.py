from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        db_table = 'clients'

class Service(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    value = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)

    class Meta:
        db_table = 'services'


class ServiceOrders(models.Model):

    order_number = models.CharField(max_length=26, blank=False, null=False)
    session_token = models.CharField(max_length=61, blank=False, null=False)
    ammount = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    date = models.DateField(blank=False, null=False)
    tx_token = models.CharField(max_length=70, blank=False, null=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False, blank=False, null=False)

    class Meta:
        db_table = 'service_orders'


