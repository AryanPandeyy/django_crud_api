from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=12)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    works = models.ManyToManyField(Work)

class Work(models.Model):
    LINK_CHOICES = [
            ('YouTube', 'YouTube'),
            ('Instagram', 'Instagram'),
            ('Other', 'Other'),
    ]
    link = models.URLField()
    work_type = models.CharField(max_length=10, choices=LINK_CHOICES)
