from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from . import forms


def login_page(request):
    log_in_form = forms.LoginForm(
        request.POST or None,
    )
    sign_in_form = forms.RegisterForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if "log_in" in request.POST:
            if log_in_form.is_valid():
                user = authenticate(
                    username=log_in_form.cleaned_data["username"],
                    password=log_in_form.cleaned_data["password"],
                )
                if user is not None:
                    login(request, user)
                    return redirect("home")
                else:
                    log_in_form.add_error(None, "Invalid username or password!")

        elif "sign_in_user" in request.POST:
            if sign_in_form.is_valid():
                user = sign_in_form.save()
                user.refresh_from_db()
                user.save()
                raw_password = sign_in_form.cleaned_data.get("password1")
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)

                # redirect user to home page
                return redirect("home")
            else:
                messages.error(request, "Error")

    return render(
        request,
        "authentication/login.html",
        context={
            "message": messages,
            "log_in_form": log_in_form,
            "sign_in_form": sign_in_form,
        },
    )


def logout_user(request):
    logout(request)
    return redirect("login")
