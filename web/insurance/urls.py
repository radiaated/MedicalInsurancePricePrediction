
from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply, name='apply'),
    path('userproposals/', views.userproposals, name='userproposals'),
    path('userproposalbyid/<int:id>/', views.userproposalbyid, name='userproposalbyid'),
    path('delete_proposal/<int:id>/', views.delete_proposal, name='userproposals'),
]
