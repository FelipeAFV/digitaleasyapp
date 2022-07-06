from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = 1
    CLIENT = 2

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (CLIENT, 'Client'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

class NewClientData(models.Model):
    id = models.IntegerField(primary_key=True)
    business_category = models.CharField(max_length=255, blank=True, null=True)
    business_creation_year = models.CharField(max_length=255, blank=True, null=True)
    business_goals = models.CharField(max_length=255, blank=True, null=True)
    business_name = models.CharField(max_length=255, blank=True, null=True)
    client_full_name = models.CharField(max_length=255, blank=True, null=True)
    ig_account = models.CharField(max_length=255, blank=True, null=True)
    more_details = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'new_client_data'

class Sample(models.Model):
    attachment = models.FileField()