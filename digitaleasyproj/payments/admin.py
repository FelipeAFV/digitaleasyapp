from django.contrib import admin
from .models import Service, ServiceOrders, Client

# Register your models here.

admin.site.register(Service)
admin.site.register(ServiceOrders)

