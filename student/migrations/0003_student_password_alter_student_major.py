# Generated by Django 4.1 on 2024-01-19 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0002_delete_enterprise_delete_student"),
        ("student", "0002_alter_student_major"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="password",
            field=models.CharField(default=123, max_length=64, verbose_name="密码"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="student",
            name="major",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="school.major",
                verbose_name="专业",
            ),
        ),
    ]