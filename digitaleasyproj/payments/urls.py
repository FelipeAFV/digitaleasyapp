from django.urls import path
from .views import createTransaction, commitTransaction, payForCustomService

urlpatterns = [
    path('', createTransaction, name='createTx'),
    path('commit', commitTransaction, name='commitTx'),
    path('createCustomService', payForCustomService, name='customPay'),
]