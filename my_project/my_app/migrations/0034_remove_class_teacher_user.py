# Generated by Django 5.1 on 2024-08-17 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0033_teacher_is_class_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class_teacher',
            name='user',
        ),
    ]
