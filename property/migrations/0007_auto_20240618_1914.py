# Generated by Django 2.2.24 on 2024-06-18 16:14

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0005_auto_20240617_2214'),
    ]

    def get_building_data(apps, schema_editor):
        Flat = apps.get_model('property', 'Flat')
        Flat.objects.all().update(new_building=models.Case(
            models.When(construction_year__gte=2015, then=True),
            default=False,
            output_field=models.BooleanField()
        ))

    operations = [
        migrations.RunPython(get_building_data)
    ]
