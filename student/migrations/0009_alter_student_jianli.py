# Generated by Django 4.1 on 2024-01-31 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0008_alter_student_limits"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="jianli",
            field=models.ImageField(
                blank=True, null=True, upload_to="jianli/", verbose_name="简历"
            ),
        ),
    ]
