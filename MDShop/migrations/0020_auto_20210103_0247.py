# Generated by Django 3.1.4 on 2021-01-02 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0019_auto_20210102_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='likecus',
        ),
        migrations.AddField(
            model_name='customer',
            name='likecus',
            field=models.ManyToManyField(default=1, null=True, to='MDShop.like'),
        ),
    ]
