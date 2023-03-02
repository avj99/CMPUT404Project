from django.contrib import admin
from .models import Post, Profile
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Post)

#Mix profile and user
class Profile(admin.StackedInline):
    model = Profile

#Extending User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # display username fields on admin page
    fields= ["username"]
    inlines=[Profile]


#Unregister inital user
admin.site.unregister(User)
#Register User and Profile
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)


