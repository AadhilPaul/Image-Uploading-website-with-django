from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpateForm, ProfileUpdateForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from main.models import Post
from django.contrib.auth.models import User

# Create your views here.

def register(response):
    form = CreateUserForm()

    if response.method == "POST":
        form = CreateUserForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            first_name = username.split()
            print(first_name)
            messages.success(response, f"Account created for {username}! You are now able to log in.")
            return redirect("login")

    context = {"form": form}
    return render(response, "register/register.html", context)


def user_profile(response, pk):
    user = User.objects.filter(id=pk).first()

    context = {
        "posts": Post.objects.filter(author=user),
        "users": user
    }
    return render(response, "register/profile.html", context)

@login_required
def profile_update(response):
    if response.method == "POST":
        user_form = UserUpateForm(response.POST, instance=response.user)
        profile_form = ProfileUpdateForm(response.POST, response.FILES, instance=response.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(response, f"Your account has been updated!")
            return redirect("user-profile", pk=response.user.id)

    else:      
        user_form = UserUpateForm(instance=response.user)
        profile_form = ProfileUpdateForm(instance=response.user.profile)

    context = {
        'u_form': user_form,
        'p_form': profile_form
    }
    return render(response, "register/profile_update.html", context)