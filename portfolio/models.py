from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач", related_name="user_portfolio")
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    surname = models.CharField(max_length=100, verbose_name="Прізвище")
    description = models.TextField(verbose_name="Короткий опис", blank=True, null=True)
    photo = models.ImageField(upload_to='media/', verbose_name="Ваше фото", blank=True, null=True)
    ins = models.URLField(verbose_name="Посилання на інстаграм", blank=True, null=True)
    github = models.URLField(verbose_name="Твій гітхаб", blank=True, null=True)
    linkedin = models.URLField(verbose_name="Твій Linkedin", blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.description}"
    
    def get_absolute_url(self):
        return reverse('portfolio_deta', args=[str(self.id)])