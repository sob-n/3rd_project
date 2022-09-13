from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class USER(AbstractUser):
    user_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)