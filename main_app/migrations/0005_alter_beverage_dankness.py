# Generated by Django 4.1 on 2022-08-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_beverage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverage',
            name='dankness',
            field=models.CharField(max_length=20),
        ),
    ]
