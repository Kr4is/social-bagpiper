# Generated by Django 4.2 on 2023-04-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0004_alter_user_profile_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_photo",
            field=models.ImageField(
                default="static/login_files/ny-img1.png", upload_to="static/"
            ),
        ),
    ]