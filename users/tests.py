from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


# Create your tests here.
class TestModels(TestCase):

    def setUp(self):
        # Main dummy user for testing 
        self.user = User.objects.create_user(username="test1",
                                    email="test1@domain.com",
                                    password="password1234567890")
        self.profile = Profile.objects.filter(user=self.user).first()
    
    # Test if the Profile is associated with the created user on creation
    def test_profile_associate_with_user_on_creation(self):
        self.assertEquals(self.profile.user, self.user)

    # Testing on linking from Profile to User model (is_active(), email)
    def test_profile_user_email_password(self):
        self.assertEquals(self.profile.user.is_active, True)   # user is not created using POST method, Django default is True
        self.assertEquals(self.profile.user.email, "test1@domain.com")

    # Test if profile_picture is default on creation
    def test_profile_picture_is_default_on_creation(self):
        self.assertEquals(self.profile.image.name, "default.jpg")
        
    # Test if image is default and is resized to 300 * 300 on save
    def test_profile_picture_is_resized(self):
        self.assertEquals(self.profile.image.height, 300)
        self.assertEquals(self.profile.image.width, 300)

    # Test if number of follows is 0
    def test_profile_follow_num_on_creation(self):
        self.assertEquals(self.profile.follows.count(), 0)