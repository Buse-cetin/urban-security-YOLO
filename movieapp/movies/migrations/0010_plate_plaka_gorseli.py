# Generated by Django 4.2.3 on 2023-11-22 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0009_plate"),
    ]

    operations = [
        migrations.AddField(
            model_name="plate",
            name="plaka_gorseli",
            field=models.ImageField(null=True, upload_to="plaka_gorselleri/"),
        ),
    ]