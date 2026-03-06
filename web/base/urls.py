from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("admin-signin/", views.AdminSignInView.as_view(), name="adminsignin"),
    path("admin-signup/", views.AdminSignUpView.as_view(), name="adminsignup"),
    path("signout/", LogoutView.as_view(next_page="home"), name="signout"),
    path("", views.index, name="home"),
]
