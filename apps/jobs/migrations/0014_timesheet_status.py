# Generated by Django 3.2.7 on 2021-09-11 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0013_auto_20210911_1628"),
    ]

    operations = [
        migrations.AddField(
            model_name="timesheet",
            name="status",
            field=models.CharField(
                choices=[
                    ("ACCEPTED", "accepted"),
                    ("DECLINED", "declined"),
                    ("CHANGED", "changed"),
                ],
                default="PENDING",
                max_length=50,
            ),
        ),
    ]
