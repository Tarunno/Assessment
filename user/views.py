from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import *

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
    
    context = {
        'title': 'Deshboard'
    }
    return render(request, 'user/deshboard.html', context)