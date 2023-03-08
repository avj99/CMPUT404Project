from django.test import TestCase
from stream.models import Post, Comment 
from django.contrib.auth.models import User
import tempfile

class testModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test1",
                                    email="test1@domain.com",
                                    password="password1234567890")
        self.post1= Post.objects.create(
            title = 'test Title',
            content = 'test content',
            #date_posted = date,
            image = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            author= self.user
            )
        self.comment1= Comment.objects.create(
            main_post = self.post1,
            name = 'test name',
            body = 'test body',
            # main_date =
        )
    #testing Posts
    def test_Post(self):
        self.assertEquals(self.post1.author,self.user)

    #testing Comments 
    def test_Comment(self):
        self.assertEquals(self.comment1.main_post,self.post1)

