from django.contrib import admin
from .models import Post, mainlikes, Comment

# Register your models here.
admin.site.register(mainlikes)
admin.site.register(Post)
admin.site.register(Comment)
