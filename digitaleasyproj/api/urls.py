
from django.urls import path, include
from .views import hello, listAllNewClients

urlpatterns = [
    path('', hello),
    path('newClients', listAllNewClients)
]