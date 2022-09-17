from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class USER(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=False)
