# Generated by Django 3.2.6 on 2021-08-25 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callbackform', '0008_alter_callback_submitted_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='submitted_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
