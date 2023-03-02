from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

'''
Example Post Format
{
    "author": "Isaac",
    "title": "Post 1",
    "content": "First post content",
    "date_posted": "Feb. 25, 2023, 6:05 p.m.",
}
'''

# render(request, page to render, context)

@user_passes_test(lambda u: not u.is_authenticated, login_url='stream-home')
def welcome(request):
    return render(request, "stream/welcome.html")


@login_required
def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "stream/home.html", context)

# See if we can filter post here
@method_decorator(login_required(login_url=reverse_lazy('welcome')), name='dispatch')
class PostListView(ListView):
    model = Post
    template_name = "stream/home.html"
    context_object_name = "posts"
    ordering = ['-date_posted']

@method_decorator(login_required(login_url=reverse_lazy('welcome')), name='dispatch')
class PostDetailView(DetailView):
    model = Post

@method_decorator(login_required(login_url=reverse_lazy('welcome')), name='dispatch')
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    # Set post author to current login user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
@method_decorator(login_required(login_url=reverse_lazy('welcome')), name='dispatch')
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

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


@method_decorator(login_required(login_url=reverse_lazy('welcome')), name='dispatch')
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    success_url = "/"

    # Check if user browsing the post is the author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
@login_required
def about(request):
    return render(request, "stream/about.html", {'title': 'About'})

