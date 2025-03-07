from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Предмет')

    def __str__(self):
        return f"{self.name}"