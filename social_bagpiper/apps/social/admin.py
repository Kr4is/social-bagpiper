from django.contrib import admin

from .models import Song, Tag, UserFollowing, Tags

class UserFollowingAdmin(admin.ModelAdmin):
    list_display = ("user_id", "following_user_id", "created")

class SongAdmin(admin.ModelAdmin):
    list_display = ("name", "uploader", "music_sheet", "upload_date", "modification_date",)

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)

class TagsAdmin(admin.ModelAdmin):
    list_display = ("song", "tag",)

admin.site.register(UserFollowing, UserFollowingAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Tags, TagsAdmin)