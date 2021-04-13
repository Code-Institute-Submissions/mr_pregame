# Generated by Django 3.1.5 on 2021-04-12 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0017_auto_20210410_0727'),
    ]

    operations = [
        migrations.CreateModel(
            name='MLBToday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.IntegerField()),
                ('schedule', models.DateTimeField()),
                ('summary', models.CharField(max_length=100)),
                ('away_team', models.CharField(max_length=100)),
                ('away_abbr', models.CharField(max_length=10)),
                ('home_team', models.CharField(max_length=100)),
                ('home_abbr', models.CharField(max_length=10)),
                ('venue', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('away_spread', models.IntegerField()),
                ('away_odds', models.IntegerField()),
                ('away_moneyline', models.IntegerField()),
                ('home_spread', models.IntegerField()),
                ('home_odds', models.IntegerField()),
                ('home_moneyline', models.IntegerField()),
                ('total', models.IntegerField()),
                ('over_odds', models.IntegerField()),
                ('under_odds', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='baseballgame',
            name='date',
            field=models.DateField(default=datetime.date(2021, 4, 11)),
        ),
        migrations.AlterField(
            model_name='startingpitcher',
            name='date',
            field=models.DateField(default=datetime.date(2021, 4, 11)),
        ),
    ]
