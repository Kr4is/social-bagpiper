from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from . import forms
from .models import Song


@login_required
def home(request):
    if request.method == "POST":
        print(request)
        if "upload_song" in request.POST:
            form = forms.SongForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                song = form.save()
                song.refresh_from_db()
                song.save()
                return redirect("home")
            else:
                message = "upload failed!"
                print(message)

        else:
            return redirect("home")

    template = loader.get_template("home.html")
    user_groups = request.user.groups.all()
    songs_to_show = {}
    songs = Song.objects.all()
    for index, song in enumerate(songs):
        songs_to_show.update({index: {"song": song, "tags": song.tags.all()}})
    following_number = request.user.following.count()
    follower_number = request.user.followers.count()
    profile_image = request.user.profile_photo.url
    context = {
        "songs": songs,
        "songs_to_show": songs_to_show,
        "user_groups": user_groups,
        "following_number": following_number,
        "follower_number": follower_number,
        "profile_image": profile_image,
    }
    return HttpResponse(template.render(context, request))