# Generated by Django 4.1.1 on 2022-09-27 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_admin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
    ]