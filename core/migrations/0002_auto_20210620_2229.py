# Generated by Django 3.1.7 on 2021-06-20 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='total',
            field=models.IntegerField(default=100000),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.TimeField(choices=[(datetime.time(6, 0), '6h00'), (datetime.time(9, 0), '9h00'), (datetime.time(18, 0), '18h00')]),
        ),
    ]
