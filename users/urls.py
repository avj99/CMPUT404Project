from django.urls import path
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

urlpatterns = [
    # Other URL patterns
    path('/', LoginView.as_view(authentication_form=CustomAuthenticationForm), name='login'),
]