# Generated by Django 2.1.7 on 2019-07-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0010_auto_20190628_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freightrate',
            name='Product_types',
            field=models.CharField(choices=[('Mineral', 'MINERAL'), ('fresh_food', 'FRESH FOOD'), ('Medicine', 'MEDICINE')], default='', max_length=254),
        ),
    ]
