# Generated by Django 5.1 on 2024-08-17 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0029_employee_class_teacher_student_hostel_attendance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.employee')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.school')),
            ],
        ),
    ]
