# Generated by Django 4.1 on 2024-01-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0002_delete_enterprise_delete_student"),
    ]

    operations = [
        migrations.AddField(
            model_name="admin",
            name="limits",
            field=models.IntegerField(
                choices=[(0, "学生"), (1, "管理员"), (2, "企业")], default=1, verbose_name="权限"
            ),
        ),
    ]
