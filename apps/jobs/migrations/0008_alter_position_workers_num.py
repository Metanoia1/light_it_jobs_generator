# Generated by Django 3.2.7 on 2021-09-10 17:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0007_auto_20210910_1741"),
    ]

    operations = [
        migrations.AlterField(
            model_name="position",
            name="workers_num",
            field=models.PositiveSmallIntegerField(
                default=1,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
    ]
