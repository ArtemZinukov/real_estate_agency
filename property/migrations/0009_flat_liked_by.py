# Generated by Django 2.2.24 on 2024-06-18 16:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0008_auto_20240618_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_flat', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
