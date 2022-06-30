from django.urls import path
from .views import createTransaction, commitTransaction, createTransactionRest

urlpatterns = [
    path('', createTransaction, name='createTx'),
    path('commit', commitTransaction, name='commitTx'),
    path('create', createTransactionRest, name='createTx2'),
]