# Generated by Django 4.1.1 on 2022-09-28 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_appointment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='test',
        ),
    ]
