from django.db import models
from django.contrib.auth.models import User
from user.models import UserX
from django.contrib.postgres.fields import ArrayField

# Create your models here.

coverage_choices = [
    ("Inpatient hospital care", "Inpatient hospital care"),
    ("Outpatient care", "Outpatient care"),
    ("Emergency services", "Emergency services"),
    ("Prescription drugs", "Prescription drugs"),
    ("Preventive services", "Preventive services"),
    ("Routine Check-ups and Vaccinations", "Routine Check-ups and Vaccinations"),
    ("Dental and Vision", "Dental and Vision"),
    ("Mental Health", "Mental Health"),
]
network_choices = [
    (
        "Access to 50+ hospitals, clinics, and healthcare providers",
        "Access to 50+ hospitals, clinics, and healthcare providers",
    ),
    (
        "Access to 100+ hospitals, clinics, and healthcare providers",
        "Access to 100+ hospitals, clinics, and healthcare providers",
    ),
    (
        "Access to 200+ hospitals, clinics, and healthcare providers",
        "Access to 200+ hospitals, clinics, and healthcare providers",
    ),
]


class CoverageOption(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Package(models.Model):
    package_name = models.CharField(max_length=500)
    coverage_limit = models.FloatField(default=0)
    premium = models.FloatField(default=0)
    deductibles = models.FloatField(default=0)
    waiting_period = models.FloatField(default=0)
    policy_period = models.FloatField(default=0)
    coverage_options = models.ManyToManyField(CoverageOption, null=True, blank=True)
    network_options = models.CharField(max_length=1000, choices=network_choices)

    def __str__(self):
        return self.package_name


class InsuranceProfile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="insurance_profile_user",
        null=False,
        blank=False,
    )
    age = models.IntegerField(default=18, null=False, blank=False, verbose_name="Age")
    sex = models.CharField(
        max_length=6,
        default="male",
        choices=[("male", "Male"), ("female", "Female")],
        verbose_name="Sex",
        null=False,
        blank=False,
    )
    region = models.CharField(
        max_length=15,
        default="southeast",
        choices=[
            ("southeast", "Southeast"),
            ("southwest", "Southwest"),
            ("northwest", "Northwest"),
            ("northeast", "Northeast"),
        ],
        verbose_name="Region",
        null=False,
        blank=False,
    )
    smoker = models.BooleanField(
        default=False,
        verbose_name="Smoker",
        null=False,
        blank=False,
    )
    children = models.IntegerField(
        default=0,
        verbose_name="Number of children",
        null=False,
        blank=False,
    )
    occupation = models.CharField(
        max_length=20,
        default="Unemployed",
        choices=[
            ("Student", "Student"),
            ("White collar", "White collar"),
            ("Blue collar", "Blue collar"),
            ("Unemployed", "Unemployed"),
        ],
        verbose_name="Occupation",
        null=False,
        blank=False,
    )
    bmi = models.FloatField(
        default=0,
        verbose_name="BMI",
        null=False,
        blank=False,
    )
    medical_history = models.CharField(
        max_length=20,
        default="No",
        choices=[
            ("Heart Disease", "Heart Disease"),
            ("High Blood Pressure", "High Blood Pressure"),
            ("No", "No"),
            ("Diabetes", "Diabetes"),
        ],
        verbose_name="Medical History",
        null=False,
        blank=False,
    )
    family_medical_history = models.CharField(
        max_length=20,
        default="No",
        choices=[
            ("Heart Disease", "Heart Disease"),
            ("High Blood Pressure", "High Blood Pressure"),
            ("No", "No"),
            ("Diabetes", "Diabetes"),
        ],
        verbose_name="Family Medical History",
        null=False,
        blank=False,
    )
    insurance_profile = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.user.username


class Proposal(models.Model):
    userx = models.ForeignKey(
        UserX,
        on_delete=models.CASCADE,
        related_name="proposal_userx",
        blank=True,
        null=True,
    )
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE, related_name="proposal_package"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    predicted_amt = models.FloatField(default=0)
    status = models.CharField(
        max_length=15,
        choices=[("accepted", "accepted"), ("rejected", "rejected")],
        null=True,
    )
    reviewed = models.BooleanField(default=False)
    insurance_profile = models.ForeignKey(
        InsuranceProfile,
        on_delete=models.CASCADE,
        related_name="insurance_profile_userx",
        blank=True,
        null=True,
    )

    confidence = models.FloatField(default=87)
