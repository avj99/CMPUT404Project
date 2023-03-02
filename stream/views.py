from time import time

from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Friends
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

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

def home(request):
    context = {
        "posts": Post.objects.all()
    }

    return render(request, "stream/home.html", context)


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
    fields = ["title", "content"]

    # Set post author to current login user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    success_url = "/"

    # Check if user browsing the post is the author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, "stream/about.html", {'title': 'About'})


def friends(request):
    res2 = Friends.objects.filter(uid=request.user.id, is_new=2).all()
    res2_1 = Friends.objects.filter(friend_id=request.user.id, is_new=2).all()

    post3temp = []
    for i in res2:
        fid = i.friend_id
        i.friend_id = User.objects.filter(id=i.friend_id).all()[0]
        i.uid = User.objects.filter(id=fid).all()[0]
        post3temp.append(i)
    print(post3temp)
    #
    for i in res2_1:
        uidt = i.friend_id
        i.uid = User.objects.filter(id=i.uid).all()[0]
        i.friend_id = User.objects.filter(id=uidt).all()[0]
        post3temp.append(i)
    print(post3temp)

    res = Friends.objects.filter(friend_id=request.user.id, is_new=1).all()
    post2temp = []
    for i in res:
        i.friend_id = User.objects.filter(id=i.friend_id).all()[0]
        i.uid = User.objects.filter(id=i.uid).all()[0]
        post2temp.append(i)
    print(post2temp)

    return render(request, "stream/friends.html",
                  {'title': 'Friends', 'friends': post3temp,
                   'posts2': post2temp})


def friends_find(request):
    id = request.GET.get("id")
    if id == "":
        return render(request, "stream/error.html",
                      {'title': 'The friend ID you entered is empty and cannot be queried'})

    if str(id) == str(request.user.id):
        return render(request, "stream/error.html",
                      {'title': "You can't add yourself as a friend"})

    print(User.objects.filter(id=id).all())
    res = User.objects.filter(id=id).all()
    if not User.objects.filter(id=id).all():
        return render(request, "stream/error.html",
                      {'title': "This ID can't be found. You can't add friends"})

    return render(request, "stream/friends_find_info.html",
                  {'title': 'Friends', 'friends': User.objects.filter(id=id).all()})


def friends_add(request):
    id = request.GET.get("id")
    if id == "":
        return render(request, "stream/error.html",
                      {'title': 'The friend ID you entered is empty and cannot be queried'})

    if str(id) == str(request.user.id):
        return render(request, "stream/error.html",
                      {'title': "You can't add yourself as a friend"})

    print(User.objects.filter(id=id).all())
    res = User.objects.filter(id=id).all()
    if not User.objects.filter(id=id).all():
        return render(request, "stream/error.html",
                      {'title': "This ID can't be found. You can't add friends"})
    # query friend
    if not Friends.objects.filter(uid=request.user.id, friend_id=id).all():
        # can add
        Friends.objects.create(uid=request.user.id, friend_id=id, is_new=1, join_date=time())
    else:
        return render(request, "stream/error.html",
                      {'title': "He is already your friend or The other party hasn't passed your friend request !!"})
    return render(request, "stream/success.html",
                  {'title': 'Add Friend Success , Please wait for the other party to pass!', 'url': '/friends'})


def friends_del(request):
    id = request.GET.get("id")
    if id == "":
        return render(request, "stream/error.html",
                      {'title': 'The friend ID you entered is empty and cannot be queried'})

    if str(id) == str(request.user.id):
        return render(request, "stream/error.html",
                      {'title': "You can't del yourself as a friend"})

    if not User.objects.filter(id=id).all():
        return render(request, "stream/error.html",
                      {'title': "This ID can't be found. You can't add friends"})
    # find has friends
    if Friends.objects.filter(
            Q(friend_id=id) | Q(uid=request.user.id) | Q(uid=id) | Q(friend_id=request.user.id)).all():
        # can del
        Friends.objects.filter(id=Friends.objects.filter(
            Q(friend_id=id) | Q(uid=request.user.id) | Q(uid=id) | Q(
                friend_id=request.user.id)).all().first().id).delete()
    else:
        return render(request, "stream/error.html",
                      {'title': "He is not your friend !!"})
    return render(request, "stream/success.html", {'title': 'Remove Friend Success!', 'url': '/friends'})


def friends_success(request):
    id = request.GET.get("id")
    if id == "":
        return render(request, "stream/error.html",
                      {'title': 'The friend ID you entered is empty and cannot be queried'})

    if str(id) == str(request.user.id):
        return render(request, "stream/error.html",
                      {'title': "You can't del yourself as a friend"})

    if not User.objects.filter(id=id).all():
        return render(request, "stream/error.html",
                      {'title': "This ID can't be found. You can't add friends"})

    if Friends.objects.filter(friend_id=request.user.id, uid=id).all():

        Friends.objects.filter(uid=id, friend_id=request.user.id).update(is_new=2)
    else:
        return render(request, "stream/error.html",
                      {'title': "He is not your friend !!"})
    return render(request, "stream/success.html", {'title': 'Success Friend Success!', 'url': '/friends'})


def friends_refuse(request):
    id = request.GET.get("id")
    if id == "":
        return render(request, "stream/error.html",
                      {'title': 'The friend ID you entered is empty and cannot be queried'})

    if str(id) == str(request.user.id):
        return render(request, "stream/error.html",
                      {'title': "You can't del yourself as a friend"})

    print(User.objects.filter(id=id).all())
    res = User.objects.filter(id=id).all()
    if not User.objects.filter(id=id).all():
        return render(request, "stream/error.html",
                      {'title': "This ID can't be found. You can't add friends"})

    if Friends.objects.filter(friend_id=request.user.id, uid=id).all():

        Friends.objects.filter(uid=id, friend_id=request.user.id).delete()
    else:
        return render(request, "stream/error.html",
                      {'title': "He is not your friend !!"})
    return render(request, "stream/success.html", {'title': 'Refuse Friend Success!', 'url': '/friends'})
