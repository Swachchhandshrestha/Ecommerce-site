# Generated by Django 2.2.6 on 2019-11-02 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopin', '0008_auto_20191102_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
