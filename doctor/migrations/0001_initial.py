# Generated by Django 4.0.5 on 2023-01-05 22:07

from django.db import migrations, models

import doctor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("clinic", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("category_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "category_name",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        validators=[doctor.models.validate_name],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                ("doctor_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "first_name",
                    models.CharField(
                        max_length=255, validators=[doctor.models.validate_name]
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=255, validators=[doctor.models.validate_name]
                    ),
                ),
                (
                    "price",
                    models.SmallIntegerField(validators=[doctor.models.validate_price]),
                ),
                ("price_description", models.TextField()),
                (
                    "exclu_price",
                    models.SmallIntegerField(validators=[doctor.models.validate_price]),
                ),
                (
                    "availability",
                    models.JSONField(validators=[doctor.models.validate_availability]),
                ),
                (
                    "language",
                    models.IntegerField(
                        choices=[(1, "Chinese"), (2, "English")], default=1
                    ),
                ),
                ("category", models.ManyToManyField(to="doctor.category")),
                ("clinic", models.ManyToManyField(to="clinic.clinic")),
            ],
        ),
    ]
