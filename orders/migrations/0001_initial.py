# Generated by Django 2.1.7 on 2019-05-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BiotechOrders',
            fields=[
                ('OrderID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('OrderDate', models.DateField()),
                ('OrderList', models.CharField(max_length=100)),
                ('Order_Payment', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FlintwoodOrders',
            fields=[
                ('OrderID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('OrderDate', models.DateField()),
                ('OrderList', models.CharField(max_length=100)),
                ('Order_Payment', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TktitanOrders',
            fields=[
                ('OrderID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('OrderDate', models.DateField()),
                ('OrderList', models.CharField(max_length=100)),
                ('Order_Payment', models.BooleanField()),
            ],
        ),
    ]
