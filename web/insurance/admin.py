from django.contrib import admin
from .models import Package, Proposal, InsuranceProfile

# Register your models here.

admin.site.register(Package)
admin.site.register(Proposal)
admin.site.register(InsuranceProfile)
