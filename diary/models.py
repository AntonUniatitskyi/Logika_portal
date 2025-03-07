from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Mark(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_marks')
    mark = models.PositiveIntegerField(verbose_name='Оцінка', validators=[MinValueValidator(1), MaxValueValidator(12)])
    subject = models.CharField(max_length=50, verbose_name='За що оцінка')

    def __str__(self):
        return f"{self.student}, {self.mark}, {self.subject}"