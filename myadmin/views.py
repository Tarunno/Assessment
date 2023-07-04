from django.shortcuts import render
from app.models import *
from user.models import *
from django.http import JsonResponse
from .models import *


def myAdmin(request):
    current_datetime = timezone.localtime(timezone.now())
    items = Item.objects.filter(end_at__gte=current_datetime).order_by('-created_at')
    item_count = len(items)
    total_value = sum([i.bid for i in items])

    users = len(User.objects.all())

    context = {
        'title': 'Admin-stats',
        'item_count': item_count,
        'total_value': total_value,
        'total_user': users
    }
    return render(request, 'myadmin/admin_deshboard.html', context)


def myAdminGallery(request):
    items = Item.objects.all().order_by('-created_at')
    context = {
        'title': 'Admin-gallery',
        'items': items
    }
    return render(request, 'myadmin/gallery.html', context)


def updateThread(request):
    last_thread = Thread.objects.all().order_by('-created_at')[0]

    print('-' * 20)

    current_datetime = timezone.localtime(timezone.now())
    auction_ended = Item.objects.filter(end_at__lt=current_datetime)
    auction_added = Item.objects.filter(end_at__gte=current_datetime)
    auction_value = sum([i.bid for i in auction_added])

    auction_added = len(auction_added)
    auction_ended = len(auction_ended)

    if auction_added != last_thread.auction_added or auction_ended != last_thread.auction_completed or auction_value != last_thread.auction_value:
        Thread.objects.create(auction_added=auction_added, auction_completed=auction_ended, auction_value=auction_value)

    threads = Thread.objects.all()
    threads = threads[len(threads)-7:]
    ls_added = [i.auction_added for i in threads]
    ls_completed = [i.auction_completed for i in threads]
    res_time = [i.created_at for i in threads]
    res_value = [i.auction_value for i in threads]

    res_added, res_completed = [ls_added[0]], [ls_completed[0]]
    for i in range(1, len(ls_added)): res_added.append(max(0, ls_added[i] - ls_added[i-1])) 
    for i in range(1, len(ls_added)): res_completed.append(max(0, ls_completed[i] - ls_completed[i-1]))

    return JsonResponse({'auction_ended': res_completed, 'auction_added': res_added, 'time': res_time, 'value': res_value})
