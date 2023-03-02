from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='stream-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='stream-about'),
    path('friends/', views.friends, name='stream-friends'),
    path('friends/find', views.friends_find, name='stream-friends-find'),
    path('friends/add', views.friends_add, name='stream-friends-add'),
    path('friends/del', views.friends_del, name='stream-friends-del'),
    path('friends/success', views.friends_success, name='stream-friends-success'),
    path('friends/refuse', views.friends_refuse, name='stream-friends-refuse'),
]
