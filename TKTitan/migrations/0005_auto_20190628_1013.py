# Generated by Django 2.1.7 on 2019-06-28 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TKTitan', '0004_auto_20190628_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_Catergory',
            field=models.CharField(default='Mineral', max_length=254),
        ),
    ]
