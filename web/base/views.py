from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from user.models import UserX
from django.contrib import messages

from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

# # Create your views here.

def index(req):

    return render(req, 'base/index.html')

def signup(req):

    
    

    if req.method == "POST":

        list(messages.get_messages(req))

        post_data = req.POST

        try:

            if User.objects.filter(username=post_data['username']).exists():
                raise Exception("Username exists")
            if User.objects.filter(email=post_data['email']).exists():
                raise Exception("Email exists")

            user = User.objects.create(
                username=post_data['username'],
                email=post_data['email'],
                
            )

            user.set_password(post_data['pwd'])

            print(user.password)
            
            userx = UserX.objects.create(
                    user=user,
                    full_name=post_data['full_name'],
                )
            
            if user and userx:
                user.save()
                userx.save()
                # msg = 'Signed up'
                
                return redirect('home')
    
        except Exception as ex:
    
            messages.error(req, ex)


            context = {
                'inp_data': post_data
            }

            return render(req, 'base/signup.html', context)

    return render(req, 'base/signup.html')


def signin(req):

    
    if req.method == "POST":

        list(messages.get_messages(req))
        post_data = req.POST

        user = authenticate(req, username=post_data['username'], password=post_data['pwd'])

        print(user)
        if user:
            login(req,user)
            return redirect("home")
        else:
            messages.error(req, "Invalid credentials")

    return render(req, 'base/signin.html')


def adminsignup(req):


    

    if req.method == "POST":
        try:
            post_data = req.POST

            if User.objects.filter(username=post_data['username']).exists():
                raise Exception("Username exists")
            if User.objects.filter(email=post_data['email']).exists():
                raise Exception("Email exists")

            user = User.objects.create(
                    username=post_data['username'],
                    email=post_data['email'],
                    is_staff=True
                )
            
            
            user.set_password(post_data['pwd'])

            print(user.password)
        

            if user:
                user.save()
            
                messages.success(req, "Signup")
                
                return redirect('home')
 
        except Exception as ex:
            messages.error(req, ex)

            context = {
                'inp_data': post_data
            }

            return render(req, 'base/adminsignup.html', context)
 

    return render(req, 'base/adminsignup.html')


def adminsignin(req):


    
    if req.method == "POST":
        post_data = req.POST
        user = authenticate(req, username=post_data['username'], password=post_data['pwd'])

        print(user)
        if user and user.is_staff == True:
            login(req,user)
            return redirect("/admins/dashboard")
        else:
            messages.error(req, "Invalid credentialss")

    return render(req, 'base/adminsignin.html')


@login_required
def signout(req):

    if req.user:
        logout(req)
        return redirect('signin')
    

