from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from ..authentication.models import User
from . import forms
from .models import Event, Group, Song


@login_required
def home(request):
    if request.method == "POST":
        print(request)
        if "upload_song" in request.POST:
            form = forms.SongForm(request.POST, request.FILES)
            if form.is_valid():
                song = Song()
                song.name = form.cleaned_data["name"]
                song.description = form.cleaned_data["description"]
                song.music_sheet = form.cleaned_data["music_sheet"]
                song.midi_file = form.cleaned_data["midi_file"]
                song.uploader = request.user
                song.save()
                return redirect("home")
            else:
                message = "song upload failed!"
        elif "upload_event" in request.POST:
            form = forms.EventForm(request.POST, request.FILES)
            if form.is_valid():
                event = Event()
                event.name = form.cleaned_data["name"]
                event.description = form.cleaned_data["description"]
                event.poster = form.cleaned_data["poster"]
                event.uploader = request.user
                event.start_date = form.cleaned_data["start_date"]
                event.end_date = form.cleaned_data["end_date"]
                event.save()
                return redirect("home")
            else:
                message = "event upload failed!"
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
    incomming_events = Event.objects.filter(end_date__gt=datetime.now())
    recommended_songs = Song.objects.filter(~Q(uploader__id=request.user.id))

    context = {
        "songs": songs,
        "songs_to_show": songs_to_show,
        "user_groups": user_groups,
        "following_number": following_number,
        "follower_number": follower_number,
        "profile_image": profile_image,
        "recommended_users": recommended_users,
        "incomming_events": incomming_events,
        "recommended_songs": recommended_songs,
    }
    return HttpResponse(template.render(context, request))


@login_required
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


@login_required
def song(request, item_id):
    song = Song.objects.get(pk=item_id)
    return render(request, "song.html", {"song": song})


@login_required
def events(request):
    template = loader.get_template("events.html")
    events_to_show = {}
    events = Event.objects.all()
    for index, event in enumerate(events):
        events_to_show.update({index: {"event": event}})

    context = {
        "events": events,
        "events_to_show": events_to_show,
    }
    return HttpResponse(template.render(context, request))


@login_required
def event(request, item_id):
    event = Event.objects.get(pk=item_id)
    return render(request, "event.html", {"event": event})


@login_required
def groups(request):
    template = loader.get_template("groups.html")
    groups_to_show = {}
    groups = Group.objects.all()
    for index, group in enumerate(groups):
        groups_to_show.update({index: {"group": group}})

    print(groups_to_show)

    context = {
        "groups": groups,
        "groups_to_show": groups_to_show,
    }
    return HttpResponse(template.render(context, request))


@login_required
def group(request, item_id):
    group = Group.objects.get(pk=item_id)
    recommended_users = User.objects.filter(~Q(id=request.user.id))

    return render(
        request,
        "group.html",
        {
            "group": group,
            "recommended_users": recommended_users,
        },
    )


@login_required
def player(request):
    template = loader.get_template("player.html")
    context = {}

    return HttpResponse(template.render(context, request))


@login_required
def profile(request, item_id):
    template = loader.get_template("profile.html")
    selected_user = User.objects.get(pk=item_id)
    songs = Song.objects.filter(Q(uploader__id=item_id))
    recommended_users = User.objects.filter(~Q(id=item_id))
    following_number = selected_user.following.count()
    follower_number = selected_user.followers.count()
    context = {
        "selected_user": selected_user,
        "songs": songs,
        "recommended_users": recommended_users,
        "following_number": following_number,
        "follower_number": follower_number,
    }

    print(songs)

    return HttpResponse(template.render(context, request))
