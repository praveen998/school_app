# Generated by Django 5.1 on 2024-08-13 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='is_present',
            field=models.BooleanField(default=False),
        ),
    ]
