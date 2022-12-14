# Generated by Django 4.1.1 on 2022-09-27 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='status',
            field=models.CharField(choices=[('occupied', 'occupied'), ('available', 'available')], default='available', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
