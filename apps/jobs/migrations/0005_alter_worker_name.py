# Generated by Django 3.2.7 on 2021-09-10 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0004_rename_workers_num_workerskill_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worker",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
