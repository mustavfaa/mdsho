# Generated by Django 3.1.4 on 2021-01-02 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0015_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='likecus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MDShop.like'),
        ),
    ]