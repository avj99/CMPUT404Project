from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

'''
messages.debug
messages.info
messages.success
messages.warning
messages.error
'''

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")
            return redirect("stream-home")

    else:
        form = UserCreationForm()
        
    return render(request, 'users/register.html', {"form": form})

