# Generated by Django 4.1 on 2024-01-20 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0005_student_end_time_student_start_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="end_time",
        ),
        migrations.RemoveField(
            model_name="student",
            name="start_time",
        ),
    ]
