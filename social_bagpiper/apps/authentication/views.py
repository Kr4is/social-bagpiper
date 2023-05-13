from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from . import forms


def login_page(request):
    message = ""
    form = None
    if request.method == "POST":
        if "log_in" in request.POST:
            form = forms.LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(
                    username=form.cleaned_data["username"],
                    password=form.cleaned_data["password"],
                )
                if user is not None:
                    login(request, user)
                    return redirect("home")
                else:
                    form.add_error(None, "Invalid username or password!")

        elif "sign_in_user" in request.POST:
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()
                user.save()
                raw_password = form.cleaned_data.get("password1")
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)

                # redirect user to home page
                return redirect("home")
            else:
                message = "SignUp failed!"

    return render(
        request, "authentication/login.html", context={"message": message, "form": form}
    )


def logout_user(request):
    logout(request)
    return redirect("login")
