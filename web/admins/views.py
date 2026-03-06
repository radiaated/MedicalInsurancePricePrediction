from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q

from insurance.models import Proposal
from .mixins import AdminRequiredMixin

# Views for admin dashboard and managing customers/proposals


class DashboardView(AdminRequiredMixin, ListView):
    """
    Displays a list of customers in the admin dashboard.
    Supports searching by first or last name.
    """

    model = User
    template_name = "admins/dashboard.html"
    context_object_name = "customers"

    def get_queryset(self):
        """Filter users by search query or return all non-staff users."""
        search = self.request.GET.get("search")
        if search:
            return (
                super()
                .get_queryset()
                .filter(
                    Q(first_name__contains=search) | Q(last_name__contains=search),
                    is_staff=False,
                )
                .order_by("first_name")[:15]
            )
        return super().get_queryset().filter(is_staff=False)


class CustomerDetailView(AdminRequiredMixin, DetailView):
    """
    Displays details of a single customer based on username.
    """

    model = User
    template_name = "admins/dashboard.html"
    context_object_name = "customer"
    slug_field = "username"
    slug_url_kwarg = "username"


class CustomerDeleteView(AdminRequiredMixin, DeleteView):
    """
    Deletes a customer and redirects to the dashboard.
    """

    model = User
    success_url = reverse_lazy("dashboard")

    def get(self, request, *args, **kwargs):
        """Override GET request to perform deletion immediately."""
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


class ProposalListView(AdminRequiredMixin, ListView):
    """
    Lists proposals for customers.
    Can filter by status; defaults to pending proposals.
    """

    model = Proposal
    template_name = "admins/customerproposals.html"
    context_object_name = "proposals"

    def get_queryset(self):
        """Filter proposals by status or return pending ones."""
        status = self.request.GET.get("status")
        if status:
            return (
                super().get_queryset().filter(status=status).order_by("-date_created")
            )
        return super().get_queryset().filter(status="pending").order_by("-date_created")


class ProposalDetailView(AdminRequiredMixin, DetailView):
    """
    Displays details of a single proposal.
    """

    model = Proposal
    template_name = "admins/customerproposalbyid.html"
    context_object_name = "proposal"


def admin_required(view_func):
    """Decorator to allow access only to admin (superuser) users."""
    return user_passes_test(lambda u: u.is_staff)(view_func)


@admin_required
def reviewproposal(request, id):
    """Mark a proposal as reviewed and update its status (admin only)."""

    proposal = Proposal.objects.get(id=id)

    proposal.status = request.GET.get("status")
    proposal.reviewed = True
    proposal.save()

    return redirect("customerproposalbyid", pk=proposal.id)
