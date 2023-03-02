from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save 
from django.urls import reverse



# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,related_name="posts", on_delete=models.CASCADE) # If user is deleted, all his/her posts are deleted
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200) # TextField can have more than 255 characters
    image = models.ImageField(upload_to="uploads/post_photo", blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True) 
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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #if user is deleted, their profile are also deleted
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical= False, blank= True )
    dateModified= models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return self.user.username

#Create profile when new user signs up
def CreateProfile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        

post_save.connect(CreateProfile, sender=User)