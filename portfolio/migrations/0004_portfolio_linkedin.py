# Generated by Django 5.1.3 on 2025-03-23 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_portfolio_ins'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='linkedin',
            field=models.URLField(blank=True, null=True, verbose_name='Твій Linkedin'),
        ),
    ]
