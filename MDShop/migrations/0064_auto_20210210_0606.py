# Generated by Django 3.1.4 on 2021-02-10 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0063_auto_20210210_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddress',
            name='address',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='apartment',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='country',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='house',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='index',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='town',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
