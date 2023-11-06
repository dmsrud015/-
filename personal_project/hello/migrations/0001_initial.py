# Generated by Django 4.2.5 on 2023-09-13 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Letter",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=20)),
                ("mess_reco", models.CharField(max_length=200)),
                ("mess_id", models.CharField(max_length=200)),
                ("mess_titles", models.CharField(max_length=200)),
                ("mess_dates", models.CharField(max_length=200)),
                ("dates", models.CharField(max_length=20)),
                ("url", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Members",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=20)),
                ("nicknames", models.CharField(max_length=20)),
                ("telnos", models.CharField(max_length=20)),
                ("dates", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="MyModel",
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
                ("upload_file", models.ImageField(upload_to="uploads/")),
            ],
        ),
        migrations.CreateModel(
            name="Snack",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
    ]
