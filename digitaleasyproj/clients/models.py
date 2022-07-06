from django.db import models
from digitaleasyproj.settings import AUTH_USER_MODEL

# Create your models here.

class Client(models.Model):

    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=35, blank=False, null=True)

    class Meta:
        db_table = 'clients'


class Business(models.Model):

    name = models.CharField(max_length=50, blank=False, null=False)
    ig_account = models.CharField(max_length=60, blank=False, null=False)
    goals = models.TextField(max_length=300, blank=False, null=False)
    creation_year = models.CharField(max_length=4, blank=False, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


    class Meta:

        db_table = 'client_business'

