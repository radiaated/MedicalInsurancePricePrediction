from django.urls import path
from . import views

urlpatterns = [
    path("apply/", views.apply, name="apply"),
    path("userproposals/", views.UserProposalListView.as_view(), name="userproposals"),
    path(
        "userproposalbyid/<int:pk>/",
        views.UserProposalDetailView.as_view(),
        name="userproposalbyid",
    ),
    path(
        "delete_proposal/<int:pk>/",
        views.UserProposalDeleteView.as_view(),
        name="userproposalsdelete",
    ),
]
