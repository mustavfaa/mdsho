# Generated by Django 3.1.1 on 2020-10-24 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
