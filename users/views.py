from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from stream.models import Post 
'''
messages.debug
messages.info
messages.success
messages.warning
messages.error
'''

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            messages.success(request, f"Your account has been created! It will need to be approved by an administrator before you can use it.")
            return redirect("register")
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        posts = Post.objects.filter()
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f"Your profile has been updated!")
            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }

    return render(request, "users/profile.html", context)