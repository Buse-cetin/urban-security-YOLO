# Generated by Django 4.2.3 on 2023-12-01 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0016_detection_plate_detection_alter_plate_options"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="plate_detection",
            new_name="PlateDetection",
        ),
    ]