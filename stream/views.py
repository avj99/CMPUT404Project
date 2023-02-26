from django.shortcuts import render
from .models import Post

'''
Example Post Format
{
    "author": "Isaac",
    "title": "Post 1",
    "content": "First post content",
    "date_posted": "Feb. 25, 2023, 6:05 p.m.",
}
'''

def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "stream/home.html", context)

def about(request):
    return render(request, "stream/about.html", {'title': 'About'})