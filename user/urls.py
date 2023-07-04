from django.urls import path
from . import views


urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('deshboard/<int:id>', views.deshboard, name='deshboard'),
    path('logout/', views.logout, name='logout'),
    path('add/', views.add_auction, name='add'),
    path('end/<int:id>', views.end_auction, name='end')
]