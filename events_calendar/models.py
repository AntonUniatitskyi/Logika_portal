from django.db import models
from home import models as home_models
from datetime import timedelta, datetime
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    subject = models.ForeignKey(home_models.Subject, on_delete=models.CASCADE)
    group = models.ForeignKey(home_models.Group, on_delete=models.CASCADE)
    description  = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def save(self, *args, **kwargs):
        if self.start_time:
            self.end_time = (datetime.combine(self.date, self.start_time) + timedelta(hours=1)).time()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.subject}, {self.date} {self.start_time} - {self.end_time}"
 
    