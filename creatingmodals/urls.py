from django.conf.urls import url
from django.urls import path
from .import views

urlpatterns = [
    path('', views.load_home, name='load_home'),
    path('load_transaction/', views.load_transaction, name='load_transaction'),
    path('load_accounts/', views.load_accounts, name='load_accounts'),
    path('load_history/', views.load_history, name='load_history'),
    path('insert_transaction/', views.insert_transaction, name='insert_transaction')
]
