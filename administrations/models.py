from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    phone_number = models.CharField(max_length=20)
    birth_date = models.DateField()