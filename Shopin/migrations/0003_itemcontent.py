# Generated by Django 2.2.6 on 2019-10-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopin', '0002_ad_brand_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itemcontent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField(blank=True)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('slug', models.TextField(max_length=300)),
                ('labels', models.CharField(blank=True, choices=[('sale', 'sale'), ('new', 'new'), ('hot', 'hot'), ('', 'default')], max_length=10)),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('', 'default')], max_length=20)),
                ('add_date', models.DateTimeField(blank=True, null=True)),
                ('stock', models.CharField(blank=True, choices=[('In Stock', 'In Stock'), ('out of Stock', 'Out of Stock')], max_length=50)),
            ],
        ),
    ]
