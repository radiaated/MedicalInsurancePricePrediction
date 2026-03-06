from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.shortcuts import render

from django.urls import reverse_lazy

from .forms import SignUpForm, AdminSignUpForm, AdminSignInForm

# # Create your views here.


def index(req):

    return render(req, "base/index.html")


def about(req):

    return render(req, "base/about.html")


def contact(req):

    return render(req, "base/contact.html")


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "base/signup.html"
    success_url = reverse_lazy("signin")


class SignInView(LoginView):

    template_name = "base/signin.html"

    def get_success_url(self):
        return reverse_lazy("home")


class AdminSignUpView(CreateView):
    form_class = AdminSignUpForm
    template_name = "base/adminsignup.html"
    success_url = reverse_lazy("adminsignin")


class AdminSignInView(LoginView):

    template_name = "base/adminsignin.html"
    authentication_form = AdminSignInForm

    def get_success_url(self):
        return reverse_lazy("dashboard")
