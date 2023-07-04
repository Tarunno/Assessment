from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def home(request):
    items = Item.objects.all().order_by('-created_at')
    context = {
        'title': 'Home',
        'items': items
    }
    return render(request, 'app/home.html', context)


def item(request, id):
    item = Item.objects.get(id=id)
    current_datetime = timezone.localtime(timezone.now())
    time_left = (item.end_at - current_datetime).total_seconds()

    bids = Bidding.objects.filter(item=id).order_by('-created_at')
    try: mini = min([i.bid for i in bids])
    except: mini = 0
              
    if time_left < 60:
        bids = Bidding.objects.filter(item=id).order_by('-bid')
        try: winner = bids[0].bidder.email
        except: winner = 'No one bidded'
        context = {
            'title': 'Item',
            'item': item,
            'bids': bids,
            'min': max(item.bid, mini),
            'end': True,
            'winner': winner
        }
        return render(request, 'app/item.html', context)

    else:
        context = {
            'title': 'Item',
            'item': item,
            'bids': bids,
            'min': max(item.bid, mini)
        }
        return render(request, 'app/item.html', context)


def place_bid(request):
    if request.method == 'POST':
        bid = request.POST.get('bid')
        item = Item.objects.get(id=int(request.POST.get('product')))
        bidder = User.objects.get(id=int(request.user.id))
        Bidding.objects.create(item=item, bid=bid, bidder=bidder)
        item.bid = bid 
        item.last_bidder = bidder
        item.save()
    return JsonResponse({'message': ['Bid placed']})