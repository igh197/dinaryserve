# Generated by Django 4.2.6 on 2023-10-24 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='download',
            name='isFinished',
            field=models.BooleanField(default=0),
        ),
    ]
