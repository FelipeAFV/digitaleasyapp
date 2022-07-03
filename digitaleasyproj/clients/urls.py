from django.urls import path
from .views import registerNewClient


urlpatterns = [
    path('signup', registerNewClient)
]