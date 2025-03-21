from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from home import models as home_models

# Create your models here.

class Mark(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_marks')
    mark = models.PositiveIntegerField(verbose_name='Оцінка', validators=[MinValueValidator(1), MaxValueValidator(12)])
    subject = models.ForeignKey(home_models.Subject, on_delete=models.CASCADE, related_name='student_subject')

    def __str__(self):
        return f"{self.student}, {self.mark}, {self.subject}"
    