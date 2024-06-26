# Generated by Django 2.2.24 on 2024-06-19 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20240618_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_flats',
            field=models.ManyToManyField(db_index=True, related_name='flat_owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owners_phonenumber',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
    ]
