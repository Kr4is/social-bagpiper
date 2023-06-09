# Generated by Django 4.2.1 on 2023-05-13 04:31

import apps.social.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("social", "0004_alter_song_options_alter_song_modification_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(null=True)),
                (
                    "poster",
                    models.FileField(upload_to=apps.social.models.event_directory_path),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("upload_date", models.DateField(auto_now_add=True)),
                ("modification_date", models.DateField(auto_now=True, db_index=True)),
                (
                    "uploader",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
