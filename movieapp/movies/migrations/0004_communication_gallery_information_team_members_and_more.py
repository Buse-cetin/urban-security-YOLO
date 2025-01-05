# Generated by Django 4.2.3 on 2023-08-02 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_example_other"),
    ]

    operations = [
        migrations.CreateModel(
            name="Communication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=200, null=True, verbose_name="Başlık"),
                ),
                (
                    "informate",
                    models.CharField(max_length=200, null=True, verbose_name="Bilgi"),
                ),
                (
                    "email",
                    models.EmailField(max_length=254, null=True, verbose_name="E-Mail"),
                ),
                ("telephone", models.IntegerField()),
                (
                    "addresss",
                    models.CharField(max_length=200, null=True, verbose_name="Adres"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Gallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "informate",
                    models.CharField(max_length=200, null=True, verbose_name="Bilgi"),
                ),
                (
                    "title",
                    models.CharField(max_length=200, null=True, verbose_name="Başlık"),
                ),
                (
                    "subtitle_one",
                    models.CharField(
                        max_length=200, null=True, verbose_name="AltBaşlık"
                    ),
                ),
                (
                    "subtitle_two",
                    models.CharField(
                        max_length=200, null=True, verbose_name="AltBaşlık"
                    ),
                ),
                (
                    "subtitle_three",
                    models.CharField(
                        max_length=200, null=True, verbose_name="AltBaşlık"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Information",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "informate",
                    models.CharField(max_length=200, null=True, verbose_name="Bilgi"),
                ),
                (
                    "title",
                    models.CharField(max_length=200, null=True, verbose_name="Başlık"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Team_Members",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=200, null=True, verbose_name="Ad"),
                ),
                (
                    "imageUrl",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Resim Url"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title_one",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Başlık 1"
                    ),
                ),
                (
                    "informate_one",
                    models.CharField(max_length=200, null=True, verbose_name="Bilgi 1"),
                ),
                (
                    "imageUrl_one",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Resim Url 1"
                    ),
                ),
                (
                    "title_two",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Başlık 2"
                    ),
                ),
                (
                    "informate_two",
                    models.CharField(max_length=200, null=True, verbose_name="Bilgi 2"),
                ),
                (
                    "imageUrl_two",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Resim Url 2"
                    ),
                ),
                (
                    "title_three",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Başlık 3"
                    ),
                ),
                (
                    "informate_three",
                    models.CharField(max_length=200, null=True, verbose_name="Bilgi 3"),
                ),
                (
                    "imageUrl_three",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Resim Url 3"
                    ),
                ),
                (
                    "title_four",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Başlık 4"
                    ),
                ),
                (
                    "informate_four",
                    models.CharField(max_length=200, null=True, verbose_name="Bilgi 4"),
                ),
                (
                    "imageUrl_four",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Resim Url 4"
                    ),
                ),
                (
                    "title_five",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Başlık 5"
                    ),
                ),
                (
                    "informate_five",
                    models.CharField(max_length=200, null=True, verbose_name="Bilgi 5"),
                ),
                (
                    "imageUrl_five",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Resim Url 5"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="about_information",
            name="imageUrl",
            field=models.ImageField(
                blank=True, null=True, upload_to="", verbose_name="Resim Url"
            ),
        ),
        migrations.AlterField(
            model_name="about_information",
            name="informate",
            field=models.CharField(max_length=200, null=True, verbose_name="Bilgi"),
        ),
        migrations.AlterField(
            model_name="about_information",
            name="title",
            field=models.CharField(max_length=200, null=True, verbose_name="Başlık"),
        ),
        migrations.AlterField(
            model_name="example",
            name="see",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="other",
            name="see",
            field=models.CharField(max_length=200, null=True),
        ),
    ]