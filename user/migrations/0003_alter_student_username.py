# Generated by Django 5.0.1 on 2024-02-01 22:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_alter_student_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="username",
            field=models.IntegerField(unique=True),
        ),
    ]
