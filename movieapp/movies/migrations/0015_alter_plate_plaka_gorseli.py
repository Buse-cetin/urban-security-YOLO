# Generated by Django 4.2.3 on 2023-11-23 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0014_alter_plate_saat_alter_plate_tarih"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plate",
            name="plaka_gorseli",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]