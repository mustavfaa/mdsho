# Generated by Django 3.1.4 on 2021-01-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0022_auto_20210104_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='likecus',
            field=models.ManyToManyField(to='MDShop.smartphone', verbose_name='b'),
        ),
    ]
