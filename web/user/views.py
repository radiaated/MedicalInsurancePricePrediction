from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserX
from django.contrib import messages
# from .forms import ProfileUserXForm, ProfileUserForm

# Create your views here.


@login_required
def profile(request):

    if request.method == "POST":
        list(messages.get_messages(request))

        try:

            post_data = request.POST
            
            print(User.objects.filter(username=post_data['username']).exclude(id=request.user.id).exists())
            print(User.objects.filter(email=post_data['email']).exclude(id=request.user.id).exists())

            if User.objects.filter(username=post_data['username']).exclude(id=request.user.id).exists():
                raise Exception("Username exists")
            if User.objects.filter(email=post_data['email']).exclude(id=request.user.id).exists():
                raise Exception("Email exists")
            print("nyo")

            user =  User.objects.get(id=request.user.id)
            userx =  UserX.objects.get(user=user)

            user.email = post_data['email']
            user.username = post_data['username']
            userx.full_name = post_data['full_name']

            

            if user and userx:
                
                user.save()
                userx.save()

                return redirect("profile")
        except Exception as ex:
            messages.error(request, ex)
            return redirect("profile")


    userx =  UserX.objects.get(user=request.user)


    context = {
        "userx": userx
    }

    return render(request, 'user/profile.html', context)

    