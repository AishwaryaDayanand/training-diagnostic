# Generated by Django 4.1.1 on 2022-09-28 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_staff_status_user_is_employee_alter_user_is_staff'),
        ('appointment', '0004_alter_appointment_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor', to='users.staff'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='lab_technician',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lab_technician', to='users.staff'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='nurse_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nurse', to='users.staff'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='sample_collector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sample_collector', to='users.staff'),
        ),
    ]