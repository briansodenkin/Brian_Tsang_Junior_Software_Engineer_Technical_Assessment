import random
from django.db import migrations, models, transaction
from faker import Faker

import doctor.models


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10**n) - 1
    return random.randint(range_start, range_end)


# Bulk create the Category
def create_default_category(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Category = apps.get_model("doctor", "Category")
    categories = [
        "General Partioner",
        "Pediatricians",
        "Internal Medicine",
        "Enternal Medicine",
        "Allergists",
        "Dermatologists",
    ]

    with transaction.atomic():
        bulk_list = list()
        for category in categories:
            bulk_list.append(Category(category_name=category))
        Category.objcdects.bulk_create(bulk_list)


# Bulk create doctor
def create_default_doctor(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    fake = Faker()
    name_list = [fake.name() for _ in range(10)]
    Clinic = apps.get_model("clinic", "Clinic")
    Category = apps.get_model("doctor", "Category")
    Doctor = apps.get_model("doctor", "Doctor")
    with transaction.atomic():
        for name in name_list:
            first_name, last_name = name.split(" ")[0], name.split(" ")[1]
            text = fake.text()
            clinic_id = random.randint(1, 9)
            clinic = Clinic.objects.filter(clinic_id=clinic_id).first()
            category_id = random.randint(1, 9)
            category = Category.objects.filter(category_id=category_id).first()
            doctor = Doctor.objects.create(
                first_name=first_name,
                last_name=last_name,
                price=random_with_N_digits(4),
                price_description=text,
                exclu_price=random_with_N_digits(4),
                availability={"monday": "1000-1800", "tuesday": "1100-1900"},
                language=random.randint(1, 2),
            )
            doctor.category.add(category)
            doctor.clinic.add(clinic)
            doctor.save()


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
        migrations.RunPython(create_default_category),
        migrations.RunPython(create_default_doctor),
    ]
