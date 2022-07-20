from django.urls import path
from .admin_views import generateCustomService

urlpatterns = [
    path('createCustomService', generateCustomService)
]