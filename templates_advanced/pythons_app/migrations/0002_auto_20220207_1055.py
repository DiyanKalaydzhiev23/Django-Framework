# Generated by Django 3.1.3 on 2022-02-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythons_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='python',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
