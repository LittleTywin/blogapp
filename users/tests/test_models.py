from django.test import TestCase
from django.test import Client
from django.core.files import File

from django.contrib.auth.models import User
from users.models import Profile

def create_user():
    return 
    

class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='asdf5tgb')

    def tearDown(self):
        try:
            self.user.delete()   
        except:
            pass

    def test_profile_image_upload(self):
        img = File(open('test_img.jpeg','rb'))
        self.user.profile.image = img
        self.user.save()

        self.assertEqual(
            self.user.profile.image,
            'prof_images/test_img.jpeg'
        )

    def test_profile_created_and_deleted_with_user(self):
        self.user.save()
        
        self.assertIsNot(self.user.profile, None)
        self.assertEqual(self.user.profile.image,'default.jpeg')
        
        self.user.delete()
        profile = Profile.objects.filter(user=self.user)

        self.assertIs(profile.count(),0)