from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import *
from .models import *


def signin(request):
    form = UserSignin(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save(request)
            print(request.user.id)
            return JsonResponse({"message": "success", "userID": request.user.id}, safe=True)
        else:
            error = form.errors
            return JsonResponse({"message": error}, safe=True)
    context = {
        'title': 'Sign in'
    }
    return render(request, 'user/signin.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect('signin')


@login_required
def deshboard(request, id):
    items = Item.objects.filter(owner=int(request.user.id))
    context = {
        'title': 'Deshboard',
        'items': items
    }
    return render(request, 'user/deshboard.html', context)


@login_required
def add_auction(request):
    if request.method == 'POST':
        form = AddAuction(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = User.objects.get(id=int(request.user.id))
            item.save()
    return JsonResponse({'message': ['Auction added']})


@login_required
def end_auction(request, id):
    item = Item.objects.get(id=id)
    if item.owner == User.objects.get(id=int(request.user.id)):
        item.end_at = timezone.localtime()
        item.save()  
    return JsonResponse({'message': ['Auction ended']})