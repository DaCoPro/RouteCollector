# Generated by Django 3.1.4 on 2020-12-28 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20201228_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='climber',
            name='routes',
            field=models.ManyToManyField(to='main_app.Route'),
        ),
    ]
