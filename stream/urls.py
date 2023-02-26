from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='stream-home'),
    path('about/', views.about, name='stream-about'),
]
