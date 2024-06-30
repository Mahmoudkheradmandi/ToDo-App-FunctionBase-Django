from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(
                    request, username=username, password=password
                )
                if user is not None:
                    auth_login(request, user)
                    return redirect("todo:home")
            else:
                return render(request, "login.html", {"form": form})

        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "login.html", context)
    else:
        return redirect("todo:home")





def register_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password1")
                user = authenticate(
                    request, username=username, password=password
                )
                if user is not None:
                    auth_login(request, user)
                return redirect("todo:home")
            else:
                return render(
                    request, "register.html", {"form": form}
                )

        form = UserCreationForm()
        context = {"form": form}
        return render(request, "register.html", context)
    else:
        return redirect("todo:home")


@login_required
def logout_user(request):
    auth_logout(request)
    return redirect("/")