from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserX(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userx_user")
    full_name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(default=18, null= True, blank=True)
    sex = models.CharField(max_length=6, default="male", choices=[("male", "Male"),("female", "Female")])
    region = models.CharField(max_length=15, default="southeast", choices=[("southeast", "Southeast"),("southwest", "Southwest"),("northwest", "Northwest"),("northeast", "Northeast")])
    
    smoker = models.BooleanField(default=True)
    children=models.IntegerField(default=0, null= True, blank=True)
    occupation=models.CharField(max_length=20, default="Unemployed", choices=[("Student",'Student'), ("White collar", 'White collar'), ("Blue collar", 'Blue collar'), ("Unemployed", 'Unemployed')])
    bmi= models.FloatField(default=0)
    medical_history = models.CharField(max_length=20, default="No", choices=[('Heart Disease', 'Heart Disease'), ('High Blood Pressure', 'High Blood Pressure'), ('No', 'No'), ('diabetes', 'Diabetes')])
    family_medical_history = models.CharField(max_length=20, default="No", choices=[('Heart Disease', 'Heart Disease'), ('High Blood Pressure', 'High Blood Pressure'), ('No', 'No'), ('diabetes', 'Diabetes')])




    def __str__(self):
        return self.full_name


