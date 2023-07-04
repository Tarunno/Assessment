from django.urls import path
from . import views

urlpatterns = [
    path('', views.myAdmin, name='my-admin')
]
