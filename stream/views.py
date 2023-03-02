from django.shortcuts import render
from .models import Post
from .models import Profile
# from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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
    if request.user.is_authenticated:
        context = {
            "posts": Post.objects.all().order_by("-date_posted")
        }
    return render(request, "stream/home.html", context)

def about(request):
    return render(request, "stream/about.html", {'title': 'About'})
# See if we can filter post here
class PostListView(ListView):
    model = Post
    template_name = "stream/home.html"
    context_object_name = "posts"
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "image"]

    # Set post author to current login user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content", "image"]

    # Set post author to current login user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # Check if user browsing the post is the author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    success_url = "/"

    # Check if user browsing the post is the author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
def profileList(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request,'stream/profileList.html', {"profiles": profiles})

def profile(request, pk):

    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id= pk)
        posts = Post.objects.filter(author_id=pk)
        if request.method == "POST":
            # Get current user ID
            current_userProfile= request.user.profile
            #Get form info
            action= request.POST['follow']
            #unfollow or follow logic
            if action =="unfollow":
                current_userProfile.follows.remove(profile)
            elif action =="follow":
                 current_userProfile.follows.add(profile)
            #Save profile info
            current_userProfile.save()
        return render(request, "stream/profile.html", {"profile":profile, "posts":posts})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page"))
        return redirect("stream-home")