from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Company(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs',null=False)  # One company can have many jobs (for total participation the foreignky has null constraint)

    def __str__(self):
        return self.title
