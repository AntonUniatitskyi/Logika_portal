from datetime import datetime
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=30, verbose_name="Им'я топіка")
    description = models.TextField(max_length=100, verbose_name="Опис топіка")
    

class Message(models.Model):
    text = models.TextField(max_length=250, verbose_name="Текст повідомлення")
    date = models.DateTimeField(default=datetime.now(), verbose_name="Дата")
    autor_id = models.IntegerField(verbose_name="Автор")
