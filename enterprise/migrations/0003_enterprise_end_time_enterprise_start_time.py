# Generated by Django 4.1 on 2024-01-20 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enterprise", "0002_enterprise_limits"),
    ]

    operations = [
        migrations.AddField(
            model_name="enterprise",
            name="end_time",
            field=models.DateTimeField(blank=True, null=True, verbose_name="结束时间"),
        ),
        migrations.AddField(
            model_name="enterprise",
            name="start_time",
            field=models.DateTimeField(blank=True, null=True, verbose_name="开始时间"),
        ),
    ]
