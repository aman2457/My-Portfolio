# Generated by Django 3.0.8 on 2020-10-05 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0002_remove_price_predictor_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price_predictor',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='price_predictor',
            name='lastname',
        ),
    ]
