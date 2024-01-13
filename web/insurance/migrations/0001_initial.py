# Generated by Django 4.2.7 on 2024-01-10 16:20

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_remove_userx_insurance_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, default=18, null=True)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=6)),
                ('region', models.CharField(choices=[('southeast', 'Southeast'), ('southwest', 'Southwest'), ('northwest', 'Northwest'), ('northeast', 'Northeast')], default='southeast', max_length=15)),
                ('smoker', models.BooleanField(default=True)),
                ('children', models.IntegerField(blank=True, default=0, null=True)),
                ('occupation', models.CharField(choices=[('Student', 'Student'), ('White collar', 'White collar'), ('Blue collar', 'Blue collar'), ('Unemployed', 'Unemployed')], default='Unemployed', max_length=20)),
                ('bmi', models.FloatField(default=0)),
                ('medical_history', models.CharField(choices=[('Heart Disease', 'Heart Disease'), ('High Blood Pressure', 'High Blood Pressure'), ('No', 'No'), ('diabetes', 'Diabetes')], default='No', max_length=20)),
                ('family_medical_history', models.CharField(choices=[('Heart Disease', 'Heart Disease'), ('High Blood Pressure', 'High Blood Pressure'), ('No', 'No'), ('diabetes', 'Diabetes')], default='No', max_length=20)),
                ('insurance_profile', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance_profile_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=500)),
                ('coverage_limit', models.FloatField(default=0)),
                ('premium', models.FloatField(default=0)),
                ('deductibles', models.FloatField(default=0)),
                ('waiting_period', models.FloatField(default=0)),
                ('policy_period', models.FloatField(default=0)),
                ('coverage_options', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=10)),
                ('network_options', models.CharField(choices=[('Access to 50+ hospitals, clinics, and healthcare providers', 'Access to 50+ hospitals, clinics, and healthcare providers'), ('Access to 100+ hospitals, clinics, and healthcare providers', 'Access to 100+ hospitals, clinics, and healthcare providers'), ('Access to 200+ hospitals, clinics, and healthcare providers', 'Access to 200+ hospitals, clinics, and healthcare providers')], max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('predicted_amt', models.FloatField(default=0)),
                ('status', models.CharField(choices=[('accepted', 'accepted'), ('rejected', 'rejected')], max_length=15, null=True)),
                ('reviewed', models.BooleanField(default=False)),
                ('insurance_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insurance_profile_userx', to='insurance.insuranceprofile')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposal_package', to='insurance.package')),
                ('userx', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposal_userx', to='user.userx')),
            ],
        ),
    ]
