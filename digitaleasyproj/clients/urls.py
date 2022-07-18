from django.urls import path
from .views import registerNewClient, getAllActiveServicesFromClient, getAllAvailableServices


urlpatterns = [
    path('signup', registerNewClient),
    path('getActiveServices', getAllActiveServicesFromClient),
    path('getAvailableServices', getAllAvailableServices)
]