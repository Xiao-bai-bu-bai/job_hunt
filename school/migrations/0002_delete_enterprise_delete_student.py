# Generated by Django 4.1 on 2024-01-19 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Enterprise",
        ),
        migrations.DeleteModel(
            name="Student",
        ),
    ]