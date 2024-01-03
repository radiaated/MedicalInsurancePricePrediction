from typing import Any
from django.db import models
from django.contrib.auth.models import User
from user.models import UserX

# Create your models here.

class Package(models.Model):
    package_name = models.CharField(max_length=500)
    coverage_limit = models.FloatField(default=0)
    premium = models.FloatField(default=0)
    deductibles = models.FloatField(default=0)
    waiting_period = models.FloatField(default=0)
    policy_period = models.FloatField(default=0)

    def __str__(self):
        return self.package_name


class InsuranceProfile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="insurance_profile_user")
    age = models.IntegerField(default=18, null= True, blank=True)
    sex = models.CharField(max_length=6, default="male", choices=[("male", "Male"),("female", "Female")])
    region = models.CharField(max_length=15, default="southeast", choices=[("southeast", "Southeast"),("southwest", "Southwest"),("northwest", "Northwest"),("northeast", "Northeast")])
    
    smoker = models.BooleanField(default=True)
    children=models.IntegerField(default=0, null= True, blank=True)
    occupation=models.CharField(max_length=20, default="Unemployed", choices=[("Student",'Student'), ("White collar", 'White collar'), ("Blue collar", 'Blue collar'), ("Unemployed", 'Unemployed')])
    bmi= models.FloatField(default=0)
    medical_history = models.CharField(max_length=20, default="No", choices=[('Heart Disease', 'Heart Disease'), ('High Blood Pressure', 'High Blood Pressure'), ('No', 'No'), ('diabetes', 'Diabetes')])
    family_medical_history = models.CharField(max_length=20, default="No", choices=[('Heart Disease', 'Heart Disease'), ('High Blood Pressure', 'High Blood Pressure'), ('No', 'No'), ('diabetes', 'Diabetes')])
    insurance_profile=models.BooleanField(default=False)



    def __str__(self):
        return self.user.username

class Proposal(models.Model):
    userx = models.ForeignKey(UserX, on_delete=models.CASCADE, related_name="proposal_userx", blank=True, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name="proposal_package")
    date_created = models.DateTimeField(auto_now_add=True)
    predicted_amt = models.FloatField(default=0)
    status = models.CharField(max_length=15, choices=[('accepted', "accepted"), ('rejected', 'rejected')], null=True)
    reviewed = models.BooleanField(default=False)
    insurance_profile = models.ForeignKey(InsuranceProfile, on_delete=models.CASCADE, related_name="insurance_profile_userx", blank=True, null=True)