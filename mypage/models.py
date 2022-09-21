import os
from django.conf import settings
from django.db import models

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    board_type = models.CharField(max_length=6)

    def __str__(self):
        return self.subject