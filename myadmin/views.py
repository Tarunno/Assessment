from django.shortcuts import render
from app.models import *

def myAdmin(request):
    current_datetime = timezone.localtime(timezone.now())
    items = Item.objects.filter(end_at__gte=current_datetime).order_by('-created_at')
    item_count = len(items)
    total_value = sum([i.bid for i in items])

    context = {
        'title': 'Admin',
        'item_count': item_count,
        'total_value': total_value
    }
    return render(request, 'myadmin/admin_deshboard.html', context)
