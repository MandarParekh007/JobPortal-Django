from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Company(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# class Job(models.Model):
