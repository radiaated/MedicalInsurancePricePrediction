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

        post_data = request.POST


        user =  User.objects.get(id=request.user.id)
        userx =  UserX.objects.get(user=user)

        user.email = post_data['email']
        user.username = post_data['username']
        userx.full_name = post_data['full_name']

        userx.smoker = True if post_data.get("smoker") else False
        
        print(userx.smoker)



        userx.age = int(float(post_data['age']))
        userx.bmi = int(float(post_data['bmi']))
        userx.children = int(float(post_data['children']))
        userx.sex = post_data['sex']
        userx.region = post_data['region']
        userx.occupation = post_data['occupation']
        userx.medical_history = post_data['medical_history']
        userx.family_medical_history = post_data['family_medical_history']

        if user and userx:
            print("yo")
            user.save()
            userx.save()

            return redirect("profile")

        
    userx =  UserX.objects.get(user=request.user)


    context = {
        "userx": userx
    }

    return render(request, 'user/profile.html', context)

    