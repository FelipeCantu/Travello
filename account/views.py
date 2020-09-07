from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username already exists...')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email already exists...')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, password = password1, first_name = first_name, last_name = last_name)
                user.save();
                print('user created successfully')
        else:
            messages.info(request, 'password don\'t match...')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')
        


