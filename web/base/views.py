from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login


from .forms import SignUpForm, AdminSignUpForm, AdminSignInForm

# Basic site pages


def index(req):
    """Render the home page."""
    return render(req, "base/index.html")


def about(req):
    """Render the about page."""
    return render(req, "base/about.html")


def contact(req):
    """Render the contact page."""
    return render(req, "base/contact.html")


# User authentication views


class SignUpView(CreateView):
    """
    User signup view.
    Displays signup form and redirects to sign-in on success.
    """

    form_class = SignUpForm
    template_name = "base/signup.html"
    success_url = reverse_lazy("signin")

    def form_valid(self, form):
        # Save the new user
        user = form.save()

        # Log the user in
        login(self.request, user)

        redirect_url = self.request.GET.get("redirect")

        if redirect_url:

            return redirect(redirect_url)

        # redirect to wherever you want logged-in users to go
        return redirect("home")


class SignInView(LoginView):
    """
    User login view.
    Redirects to home page after successful login.
    """

    template_name = "base/signin.html"

    def get_success_url(self):
        """Return the URL to redirect to after login."""
        return reverse_lazy("home")


class AdminSignUpView(CreateView):
    """
    Admin signup view.
    Displays admin signup form and redirects to admin sign-in on success.
    """

    form_class = AdminSignUpForm
    template_name = "base/adminsignup.html"
    success_url = reverse_lazy("adminsignin")

    def form_valid(self, form):
        # Save the new user
        user = form.save()

        # Log the user in
        login(self.request, user)

        # redirect to wherever you want logged-in users to go
        return redirect("dashboard")


class AdminSignInView(LoginView):
    """
    Admin login view.
    Uses custom authentication form and redirects to dashboard on success.
    """

    template_name = "base/adminsignin.html"
    authentication_form = AdminSignInForm

    def get_success_url(self):
        """Return the URL to redirect to after admin login."""
        return reverse_lazy("dashboard")
