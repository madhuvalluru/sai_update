# Generated by Django 2.2 on 2019-11-24 13:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('saiapp', '0008_auto_20191124_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register1',
            name='creates',
            field=models.DateField(default=datetime.datetime(2019, 11, 24, 13, 55, 30, 566745, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='register1',
            name='rgid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
