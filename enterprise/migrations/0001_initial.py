# Generated by Django 4.1 on 2024-01-19 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Enterprise",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32, verbose_name="企业名称")),
                ("address", models.CharField(max_length=32, verbose_name="企业地址")),
                ("phone", models.CharField(max_length=32, verbose_name="企业电话")),
                ("email", models.CharField(max_length=32, verbose_name="企业邮箱")),
                ("password", models.CharField(max_length=64, verbose_name="企业密码")),
                (
                    "media",
                    models.FileField(
                        blank=True, null=True, upload_to="media/", verbose_name="简历"
                    ),
                ),
            ],
        ),
    ]
