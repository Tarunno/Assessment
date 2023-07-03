from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('item/<int:id>', views.item, name='item'),
    path('bid/', views.place_bid, name='place-bid')
]