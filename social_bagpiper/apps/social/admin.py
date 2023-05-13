from django.contrib import admin

from .models import Event, Song, Tag, Tags, UserFollowing


class UserFollowingAdmin(admin.ModelAdmin):
    list_display = ("user_id", "following_user_id", "created")


class SongAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "uploader",
        "music_sheet",
        "upload_date",
        "modification_date",
    )


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


class TagsAdmin(admin.ModelAdmin):
    list_display = (
        "song",
        "tag",
    )


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "uploader",
        "poster",
        "upload_date",
        "modification_date",
        "start_date",
        "end_date",
    )


admin.site.register(UserFollowing, UserFollowingAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Event, EventAdmin)
