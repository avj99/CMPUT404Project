from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from stream.models import Post

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical= False, blank= True )

    def __str__(self):
        return f"{self.user.username} Profile"

    # Run after model is saved
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)  # open the current instance
        if img.height > 300 or img.width > 300:
            new_size = (300, 300)
            img.thumbnail(new_size)
            img.save(self.image.path)