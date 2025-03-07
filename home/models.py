from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=45)
    
class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Предмет')

    def __str__(self):
        return f"{self.name}"
