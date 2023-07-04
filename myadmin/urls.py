from django.urls import path
from . import views

urlpatterns = [
    path('', views.myAdmin, name='my-admin'),
    path('update-thread/', views.updateThread, name='update-thread'),
    path('gallery/', views.myAdminGallery, name='admin-gallery')
]
