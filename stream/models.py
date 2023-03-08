from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()                               # TextField can have more than 255 characters
    date_posted = models.DateTimeField(default=timezone.now) 
    '''https://www.youtube.com/watch?v=xqFM6ykQEwo'''
    howManyLike = models.ManyToManyField(User,related_name= "howManyLike")
    image = models.ImageField(upload_to="uploads/post_photo", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # If user is deleted, all his/her posts are deleted


    def __str__(self):
        return (
            f"{self.author}"
            f"({self.date_posted:%Y-%m-%d %H:%M}): "
            f"{self.title}"
            f"{self.content}"
            f"{self.image}"
        )    

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    def likes(self):
        return self.howManyLike
    
# https://www.youtube.com/watch?v=OuOB9ADT_bo
# link the 33 video too
class Comment(models.Model):
    main_post = models.ForeignKey(Post, related_name = "main_comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # they are just big boxes
    body = models.TextField()
    main_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s  : %s' % (self.main_post.title, self.main_name)
    
    def get_absolute_url(self):
        return reverse("stream-home")

class mainlikes(models.Model):
    mainUser = models.ForeignKey(User, on_delete=models.CASCADE)
    mainint = models.CharField(default = "Like", max_length= 5)
    mainPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.mainPost)
    
