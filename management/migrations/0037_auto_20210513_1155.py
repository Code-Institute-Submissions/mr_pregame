# Generated by Django 3.1.5 on 2021-05-13 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0036_auto_20210513_0317'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basketballteamstats',
            options={'verbose_name_plural': 'Basketball team stats'},
        ),
        migrations.AlterModelOptions(
            name='teamname',
            options={'verbose_name_plural': 'Teams'},
        ),
    ]