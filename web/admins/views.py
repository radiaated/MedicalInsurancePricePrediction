from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from user.models import UserX
from django.contrib import messages
from insurance.models import Proposal

from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

# # Create your views here.

def dashboard(req):
    

    userx = UserX.objects.all().order_by("full_name")[:15]

    if(req.method == "POST"):
         userx = UserX.objects.filter(full_name__contains=req.POST['search']).order_by("full_name")[:15]

    print(userx)

    context = {
        'userx': userx
    }

    return render(req, 'admins/dashboard.html', context)

def customerinfo(req, username):
    

    userx = UserX.objects.get(user__username=username)

    
    print(userx)

    context = {
        'userx': userx
    }

    return render(req, 'admins/customerprofile.html', context)


def customerproposals(req):
    

    if req.method == 'GET':
        reviewed = False
        status = None
        proposals = Proposal.objects.filter(reviewed=reviewed)[:15]
    elif req.method == 'POST':
        print(req.POST)

        status = req.POST.get('status') if req.POST.get('status') else None

        if status:
            reviewed=True
            proposals = Proposal.objects.filter(status=status, reviewed =reviewed)[:15]
        else:
            reviewed = (True if req.POST['reviewed'] == 'on' else False) if req.POST.get('reviewed') else False
            proposals = Proposal.objects.filter(reviewed=reviewed)[:15]
        

        
        
    print(reviewed)     
    print(status)     


    context = {
        'proposals': proposals,
        'status': status,
        'reviewed': reviewed
    }

    return render(req, 'admins/customerproposals.html', context)


def customerproposalbyid(req, id):
    

    if req.method == 'GET':
        proposal = Proposal.objects.get(id=id)
    elif req.method == 'POST':
        pass


    context = {
        'proposal': proposal
    }

    return render(req, 'admins/customerproposalbyid.html', context)


def delete_customer(req, id):
    

    User.objects.delete(id=id)



def reviewproposal(request, id):
    proposal = Proposal.objects.get(id=id)

   

    proposal.status = request.GET.get("status")
    proposal.reviewed = True
    proposal.save()

    return redirect("customerproposalbyid", id=proposal.id)

