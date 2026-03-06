from django.urls import path

from . import views

urlpatterns = [
    path("profile/", views.UserProfileUpdateView.as_view(), name="profile"),
]
