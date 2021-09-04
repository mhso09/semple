from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def main(request):
    if request.method =='GET' :
        return render(request, 'users/main.html')
    
    if request.method == 'POST' :
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('posts:index'))
    return render(request, 'users/main.html')
