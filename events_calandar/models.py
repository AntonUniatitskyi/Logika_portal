from django.db import models
from home import models as home_models
from datetime import timedelta, datetime

# Create your models here.
class Event(models.Model):
    subject = models.ForeignKey(home_models.Subject, on_delete=models.CASCADE)
    group = models.ForeignKey(home_models.Group, on_delete=models.CASCADE)
    description  = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()