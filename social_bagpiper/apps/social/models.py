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


def midi_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<uploader>/<name>
    return f"midi_file/{instance.uploader.id}/{instance.name}.mid"


def mp3_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<uploader>/<name>
    return f"midi_file/{instance.uploader.id}/{instance.name}.mp3"


class Song(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    views = models.IntegerField(default=0)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    music_sheet = models.FileField(upload_to=song_directory_path)
    midi_file = models.FileField(upload_to=midi_directory_path, null=True)
    mp3_file = models.FileField(upload_to=mp3_directory_path, null=True)
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


def event_directory_path(instance, filename):
    return f"events/{instance.uploader.id}/{instance.name}.png"


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    poster = models.FileField(upload_to=event_directory_path)
    start_date = models.DateField()
    end_date = models.DateField()
    upload_date = models.DateField(auto_now_add=True)
    modification_date = models.DateField(auto_now=True, db_index=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.name} by {self.uploader}"


class Group(models.Model):
    name = models.CharField(max_length=128)
    profile_photo = models.ImageField(default="default.jpg", upload_to="groups_images")
    creation_date = models.DateField(auto_now_add=True, null=True)
    users = models.ManyToManyField(
        User,
        through="Membership",
        through_fields=("group", "user"),
    )

    def __str__(self):
        return f"{self.name}"


class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )

    def __str__(self):
        return f"{self.user} at {self.group} by {self.inviter}"
