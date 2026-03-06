from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Q

from insurance.models import Proposal
from .mixins import AdminRequiredMixin

# # Create your views here.


class DashboardView(AdminRequiredMixin, ListView):
    model = User
    template_name = "admins/dashboard.html"
    context_object_name = "customers"

    def get_queryset(self):
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
    model = User
    template_name = "admins/dashboard.html"
    context_object_name = "customer"

    slug_field = "username"
    slug_url_kwarg = "username"


class CustomerDeleteView(AdminRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("dashboard")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


class ProposalListView(AdminRequiredMixin, ListView):
    model = Proposal
    template_name = "admins/customerproposals.html"
    context_object_name = "proposals"

    def get_queryset(self):

        status = self.request.GET.get("status")

        if status:

            return super().get_queryset().filter(status=status).order_by("date_created")

        return super().get_queryset().filter(status="pending").order_by("date_created")


class ProposalDetailView(AdminRequiredMixin, DetailView):
    model = Proposal
    template_name = "admins/customerproposalbyid.html"
    context_object_name = "proposal"
