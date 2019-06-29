# Generated by Django 2.1.7 on 2019-06-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0004_auto_20190624_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='freightrate',
            name='From_port_to_destination_freight',
            field=models.CharField(choices=[('air', 'AIR'), ('sea', 'SEA'), ('road', 'ROAD')], default='', max_length=254),
        ),
        migrations.AddField(
            model_name='freightrate',
            name='From_source_to_Port_freight',
            field=models.CharField(choices=[('air', 'AIR'), ('sea', 'SEA'), ('road', 'ROAD')], default='', max_length=254),
        ),
    ]
