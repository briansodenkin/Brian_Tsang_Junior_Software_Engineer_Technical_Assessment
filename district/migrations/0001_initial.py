# Generated by Django 4.0.5 on 2023-01-05 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="District",
            fields=[
                ("district_id", models.AutoField(primary_key=True, serialize=False)),
                ("district_name", models.CharField(max_length=255)),
            ],
        ),
    ]