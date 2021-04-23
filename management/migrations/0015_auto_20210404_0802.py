# Generated by Django 3.1.5 on 2021-04-04 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_baseballgame_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseballgame',
            name='bullpen_innings',
        ),
        migrations.RemoveField(
            model_name='startingpitcher',
            name='innings',
        ),
        migrations.AddField(
            model_name='baseballgame',
            name='bullpen_inning_thirds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='startingpitcher',
            name='inning_thirds',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]