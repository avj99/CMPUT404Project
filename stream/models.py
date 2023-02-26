from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()                               # TextField can have more than 255 characters
    date_posted = models.DateTimeField(default=timezone.now) 
    author = models.ForeignKey(User, on_delete=models.CASCADE) # If user is deleted, all his/her posts are deleted

    def __str__(self):
        return self.title

