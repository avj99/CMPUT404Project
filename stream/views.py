from django.shortcuts import render

posts = [
    {
        "author": "Isaac",
        "title": "Post 1",
        "content": "First post content",
        "date_posted": "Feb 25, 2023",
    },
    {
        "author": "User 2",
        "title": "Post 2",
        "content": "Second post content",
        "date_posted": "Feb 26, 2023",
    }
]

# Create your views here.
def home(request):
    context = {
        "posts": posts
    }
    return render(request, "stream/home.html", context)

def about(request):
    return render(request, "stream/about.html", {'title': 'About'})