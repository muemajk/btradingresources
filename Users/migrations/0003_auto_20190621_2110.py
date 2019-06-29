# Generated by Django 2.1.7 on 2019-06-21 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20190621_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='privilege',
            field=models.CharField(choices=[('flintwood', 'FLINTWOOD'), ('biotech', 'BIOTECH'), ('tktitan', 'TKTITAN'), ('all', 'ALL'), ('none', 'NONE')], default='none', max_length=30),
        ),
        migrations.AlterField(
            model_name='client',
            name='role',
            field=models.CharField(choices=[('buyer', 'BUYER'), ('Flintwood_supplier', 'FLINTWOOD SUPPLIER'), ('btsupplier', 'BTTITAN SUPPLIER'), ('biotec_supplier', 'BIOTEC SUPPLIER')], default='buyer', max_length=10),
        ),
    ]
