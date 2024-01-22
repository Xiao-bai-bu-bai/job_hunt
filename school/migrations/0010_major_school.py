# Generated by Django 4.1 on 2024-01-21 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0009_alter_schoolmajor_major_alter_schoolmajor_school"),
    ]

    operations = [
        migrations.AddField(
            model_name="major",
            name="school",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="school.school",
                verbose_name="学校",
            ),
        ),
    ]