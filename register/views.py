from django.shortcuts import render
from django.contrib import messages
from .models import *


from django.contrib.auth import authenticate, login


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')




def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        pro_obj = Profile.objects.create(name = name, username = username, email = email, phone = phone, password= password)
        print(pro_obj, "hey")
        pro_obj.save()
        

        return redirect('login')

    else:
        return render(request, 'signup.html')