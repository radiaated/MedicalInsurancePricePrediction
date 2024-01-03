
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('admin-signin/', views.adminsignin, name='adminsignin'),
    path('admin-signup/', views.adminsignup, name='adminsignup'),
    path('signout/', views.signout, name='signout'),
    path('', views.index, name='home'),
]
