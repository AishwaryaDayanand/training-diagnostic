# Generated by Django 4.1.1 on 2022-09-28 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0009_appointment_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]