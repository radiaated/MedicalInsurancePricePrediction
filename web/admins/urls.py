
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('c-<str:username>/', views.customerinfo, name='customerprofile'),
    path('customerproposals/', views.customerproposals, name='customerproposals'),
    path('customerproposal/<int:id>/', views.customerproposalbyid, name='customerproposalbyid'),
    path('reviewproposal/<int:id>/', views.reviewproposal, name='reviewproposal'),

]
