# Generated by Django 5.1 on 2024-08-16 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_app', '0012_remove_student_school_remove_teacher_model_school_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('contact', models.CharField(max_length=20)),
                ('school_admin_first_name', models.CharField(max_length=100)),
                ('school_admin_last_name', models.CharField(max_length=100)),
                ('school_admin_username', models.CharField(max_length=150)),
            ],
        ),
    ]
