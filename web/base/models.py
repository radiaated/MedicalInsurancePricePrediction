from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserX(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userx_user")

    

    full_name = models.CharField(max_length=50, null=False, blank=False)

    age = models.IntegerField(default=18)

    def __str__(self):
        return self.full_name