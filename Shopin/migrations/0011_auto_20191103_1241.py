# Generated by Django 2.2.6 on 2019-11-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopin', '0010_auto_20191102_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, upload_to='brands'),
        ),
    ]
