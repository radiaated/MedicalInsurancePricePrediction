from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path(
        "customer/<str:username>/",
        views.CustomerDetailView.as_view(),
        name="customerprofile",
    ),
    path(
        "deletecustomer/<int:pk>/",
        views.CustomerDeleteView.as_view(),
        name="deletecustomer",
    ),
    path(
        "customerproposals/", views.ProposalListView.as_view(), name="customerproposals"
    ),
    path(
        "customerproposal/<int:pk>/",
        views.ProposalDetailView.as_view(),
        name="customerproposalbyid",
    ),
]
