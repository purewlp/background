# Generated by Django 4.1.7 on 2023-05-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatarUrl",
            field=models.CharField(default="", max_length=1024),
        ),
    ]
