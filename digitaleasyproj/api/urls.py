
from django.urls import path, include
from .views import hello, listAllNewClients, deleteClient

urlpatterns = [
    path('', hello),
    path('newClients', listAllNewClients),
    path('newClients/delete/<int:id>', deleteClient),
    path('admin/', include('api.admin_urls'))
]