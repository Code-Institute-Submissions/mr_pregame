# Generated by Django 3.1.5 on 2021-04-15 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0019_auto_20210414_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseballgame',
            name='date',
            field=models.DateField(default=datetime.date(2021, 4, 14)),
        ),
        migrations.AlterField(
            model_name='startingpitcher',
            name='date',
            field=models.DateField(default=datetime.date(2021, 4, 14)),
        ),
    ]