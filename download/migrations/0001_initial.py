# Generated by Django 4.2.6 on 2023-10-18 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DownLoad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(upload_to='./media')),
                ('color', models.ImageField(upload_to='./media')),
                ('summed', models.FileField(upload_to='./media/result')),
            ],
        ),
    ]