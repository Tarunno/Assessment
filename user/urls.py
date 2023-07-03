from django.urls import path
from . import views


urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('deshboard/<int:id>', views.deshboard, name='deshboard'),
    path('logout/', views.logout, name='logout')
]