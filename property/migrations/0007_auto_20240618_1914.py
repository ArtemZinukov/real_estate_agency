# Generated by Django 2.2.24 on 2024-06-18 16:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0005_auto_20240617_2214'),
    ]

    def get_building_data(apps, schema_editor):
        Flat = apps.get_model('property', 'Flat')
        for flat in Flat.objects.all():
            flat.new_building = flat.construction_year >= 2015
            flat.save()

    operations = [
        migrations.RunPython(get_building_data)
    ]