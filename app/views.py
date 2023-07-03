from django.shortcuts import render
from .models import *

def home(request):
    items = Item.objects.all().order_by('-created_at')

    context = {
        'title': 'Home',
        'items': items
    }
    return render(request, 'app/home.html', context)