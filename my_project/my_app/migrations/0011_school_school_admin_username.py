# Generated by Django 5.1 on 2024-08-14 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_student_school_teacher_model_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='school_admin_username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
