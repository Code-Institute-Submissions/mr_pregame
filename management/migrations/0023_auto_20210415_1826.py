# Generated by Django 3.1.5 on 2021-04-15 18:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0022_auto_20210415_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='mlbgameline',
            name='gameday',
            field=models.DateTimeField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mlbgameline',
            name='pick',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mlbgameline',
            name='pick_type',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
