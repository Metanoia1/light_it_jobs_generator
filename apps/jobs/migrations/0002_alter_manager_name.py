# Generated by Django 3.2.7 on 2021-09-10 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manager",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
