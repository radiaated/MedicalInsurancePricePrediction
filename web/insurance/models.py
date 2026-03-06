from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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
    coverage_limit = models.FloatField(
        default=0,
        null=False,
        blank=False,
    )
    premium = models.FloatField(
        default=0,
        null=False,
        blank=False,
    )
    deductibles = models.FloatField(
        default=0,
        null=False,
        blank=False,
    )
    waiting_period = models.FloatField(
        default=0,
        null=False,
        blank=False,
    )
    policy_period = models.FloatField(
        default=0,
        null=False,
        blank=False,
    )
    coverage_options = models.ManyToManyField(
        CoverageOption,
    )
    network_options = models.CharField(
        max_length=1000,
        choices=network_choices,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.package_name


class InsuranceProfile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_insurance_profiles",
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        default=18,
        validators=[MinValueValidator(18), MaxValueValidator(64)],
        null=False,
        blank=False,
        verbose_name="Age",
    )
    gender = models.CharField(
        max_length=6,
        default="male",
        choices=[("male", "Male"), ("female", "Female")],
        verbose_name="Gender",
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
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        null=False,
        blank=False,
        verbose_name="Number of children",
    )
    occupation = models.CharField(
        max_length=20,
        default="Unemployed",
        choices=[
            ("Student", "Student"),
            ("Unemployed", "Unemployed"),
            ("White collar", "White collar"),
            ("Blue collar", "Blue collar"),
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
        default="no",
        choices=[
            ("no", "No"),
            ("Heart disease", "Heart disease"),
            ("High blood pressure", "High blood pressure"),
            ("Diabetes", "Diabetes"),
        ],
        verbose_name="Medical History",
        null=False,
        blank=False,
    )
    family_medical_history = models.CharField(
        max_length=20,
        default="no",
        choices=[
            ("no", "No"),
            ("Heart disease", "Heart disease"),
            ("High blood pressure", "High blood pressure"),
            ("Diabetes", "Diabetes"),
        ],
        verbose_name="Family Medical History",
        null=False,
        blank=False,
    )
    exercise_frequency = models.CharField(
        max_length=12,
        default="No",
        choices=[
            ("Never", "Never"),
            ("Occasionally", "Occasionally"),
            ("Rarely", "Rarely"),
            ("Frequently", "Frequently"),
        ],
        verbose_name="Exercise Frequency",
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

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name="package_proposals",
        null=False,
        blank=False,
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
    )
    predicted_amt = models.FloatField(
        default=0,
        null=False,
        blank=False,
    )
    status = models.CharField(
        max_length=15,
        choices=[
            ("pending", "pending"),
            ("accepted", "accepted"),
            ("rejected", "rejected"),
        ],
        default="pending",
        null=False,
        blank=False,
    )
    reviewed = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    insurance_profile = models.ForeignKey(
        InsuranceProfile,
        on_delete=models.CASCADE,
        related_name="insurance_profile_proposal",
        null=False,
        blank=False,
    )
