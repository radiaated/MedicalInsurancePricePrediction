from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserX
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(req):

    return render(req, 'base/index.html')

def signup(req):

    msg=''
    

    if req.method == "POST":
        post_data = req.POST
        print(post_data['username'])

        user = User.objects.create(
                username=post_data['username'],
                
            )
        
        
        user.set_password(post_data['pwd'])

        print(user.password)
        
        userx = UserX.objects.create(
                user=user,
                full_name=post_data['full_name'],
                age=post_data['age'],
            )
        
        if user and userx:
            user.save()
            userx.save()
            # msg = 'Signed up'
            messages.success(req, "Signup")
            
            return redirect('home')
 
    context = {"msg": msg}

    return render(req, 'base/signup.html', context)


def signin(req):

    msg=''
    

    if req.method == "POST":
        post_data = req.POST
        user = authenticate(req, username=post_data['username'], password=post_data['pwd'])

        print(user)
        if user:
            login(req,user)
            return redirect("home")
        else:
            messages.error(req, "Invalid credentials")

    return render(req, 'base/signin.html')


@login_required
def signout(req):

    if req.user:
        logout(req)
        return redirect('signin')
