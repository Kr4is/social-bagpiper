from django.db import models

from ..authentication.models import User


class UserFollowing(models.Model):
    user_id = models.ForeignKey(
        User, related_name="following", on_delete=models.CASCADE
    )
    following_user_id = models.ForeignKey(
        User, related_name="followers", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user_id", "following_user_id"], name="unique_followers"
            )
        ]
        ordering = ["-created"]

    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


def song_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<uploader>/<name>
    return f"music_sheets/{instance.uploader.id}/{instance.name}.pdf"


class Song(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    music_sheet = models.FileField(upload_to=song_directory_path)
    upload_date = models.DateField(auto_now_add=True)
    modification_date = models.DateField(auto_now=True, db_index=True)
    tags = models.ManyToManyField(
        Tag,
        through="Tags",
        through_fields=("song", "tag"),
    )

    class Meta:
        ordering = ["-modification_date"]

    def __str__(self):
        return f"{self.name} by {self.uploader}"


class Tags(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="tagged_song")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.song} is {self.tag}"
