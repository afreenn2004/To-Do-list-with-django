#AfreenAjaz
from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.first().id)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

