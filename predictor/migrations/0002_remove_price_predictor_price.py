# Generated by Django 3.0.8 on 2020-10-05 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price_predictor',
            name='price',
        ),
    ]
