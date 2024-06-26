# Generated by Django 4.1 on 2024-01-19 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("school", "0002_delete_enterprise_delete_student"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "Student_ID",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="学号"
                    ),
                ),
                ("name", models.CharField(max_length=32, verbose_name="姓名")),
                ("age", models.IntegerField(blank=True, null=True, verbose_name="年龄")),
                (
                    "gender",
                    models.IntegerField(
                        choices=[(1, "男"), (2, "女")], default=1, verbose_name="性别"
                    ),
                ),
                (
                    "media",
                    models.FileField(
                        blank=True, null=True, upload_to="media/", verbose_name="简历"
                    ),
                ),
                (
                    "major",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="school.major",
                        verbose_name="专业",
                    ),
                ),
            ],
        ),
    ]
