from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import UserProfileForm

# View to update the logged-in user's profile


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    Allows a logged-in user to update their profile information.
    """

    model = User
    form_class = UserProfileForm
    template_name = "user/profile.html"
    success_url = reverse_lazy("profile")
    login_url = reverse_lazy("signin")

    def get_object(self, queryset=None):
        """Return the current logged-in user as the object to update."""
        return self.request.user
