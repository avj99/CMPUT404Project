from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy, reverse 
from django.http import HttpResponseRedirect
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
    fields = ["title", "content","image"]

    # Set post author to current login user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
@method_decorator(login_required(login_url=reverse_lazy('welcome')), name='dispatch')
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content","image"]

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

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["name", "body"]

    # Set post author to current login user
    def form_valid(self, form):
        form.instance.main_post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    
@login_required
def about(request):
    return render(request, "stream/about.html", {'title': 'About'})

'''def post_liked(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    post.howManyLike.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args = [str(pk)]))

    mainuser = request.user
    print(post.id)
    if (request.method == 'GET'):
        id_post = request.get('id_post')
        post_post = Post.objects.get(id='id_post')

        if mainuser in post_post.howManyLike.all():
            post_post.remove(mainuser)
        else:
            post_post.add(mainuser)

    return redirect('stream:stream-home')''' 

