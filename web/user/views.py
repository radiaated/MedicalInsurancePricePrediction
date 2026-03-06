from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .forms import UserProfileForm

# Create your views here.


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "user/profile.html"
    success_url = reverse_lazy("profile")
    login_url = reverse_lazy("signin")

    def get_object(self, queryset=None):

        return self.request.user
