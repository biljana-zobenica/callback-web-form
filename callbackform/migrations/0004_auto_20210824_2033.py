# Generated by Django 3.2.6 on 2021-08-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callbackform', '0003_callbackform_submitted_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callbackform',
            name='archive',
        ),
        migrations.AddField(
            model_name='callbackform',
            name='status',
            field=models.CharField(choices=[('o', 'Outstanding'), ('a', 'Archived')], default='Not reviewed', max_length=1),
        ),
    ]
