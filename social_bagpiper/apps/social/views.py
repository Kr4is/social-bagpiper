from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from ..authentication.models import User
from . import forms
from .models import Song


@login_required
def home(request):
    if request.method == "POST":
        print(request)
        if "upload_song" in request.POST:
            form = forms.SongForm(request.user, request.POST, request.FILES)
            if form.is_valid():
                song = Song()
                song.name = form.cleaned_data["name"]
                song.description = form.cleaned_data["description"]
                song.music_sheet = form.cleaned_data["music_sheet"]
                song.uploader = request.user
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
    recommended_users = User.objects.filter(~Q(id=request.user.id))

    context = {
        "songs": songs,
        "songs_to_show": songs_to_show,
        "user_groups": user_groups,
        "following_number": following_number,
        "follower_number": follower_number,
        "profile_image": profile_image,
        "recommended_users": recommended_users,
    }
    return HttpResponse(template.render(context, request))


def songs(request):
    template = loader.get_template("songs.html")
    songs_to_show = {}
    songs = Song.objects.all()
    for index, song in enumerate(songs):
        songs_to_show.update({index: {"song": song, "tags": song.tags.all()}})

    context = {
        "songs": songs,
        "songs_to_show": songs_to_show,
    }
    return HttpResponse(template.render(context, request))


def song(request, item_id):
    song = Song.objects.get(pk=item_id)
    return render(request, "song.html", {"song": song})


def profile(request):
    template = loader.get_template("profile.html")
    songs = Song.objects.filter(Q(uploader__id=request.user.id))
    context = {"songs": songs}

    return HttpResponse(template.render(context, request))
