# Generated by Django 2.1.7 on 2019-06-28 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0007_auto_20190627_1047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freightrate',
            old_name='QuantityRecieved',
            new_name='MaxQuantityRecieved',
        ),
        migrations.RenameField(
            model_name='freightrate',
            old_name='QuantitySent',
            new_name='MaxQuantitySent',
        ),
        migrations.AddField(
            model_name='freightrate',
            name='MiniQuantityRecieved',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='freightrate',
            name='MiniQuantitySent',
            field=models.IntegerField(default=1),
        ),
    ]
