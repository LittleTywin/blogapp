from django.test import TestCase
from PIL import Image
from users.forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm

class TestForms(TestCase):

    def setUp(self):
        pass



    def test_UserRegisterForm_valid(self):
        form = UserRegisterForm({
            'username' :'testuser',
            'password1' : 'wikidiki',
            'password2': 'wikidiki'
        })
        self.assertIs(form.is_valid(), True)
    
    def test_UserRegisterForm_not_valid(self):
        form = UserRegisterForm({
            'username' :'testuser',
            'password1' : 'wikidiki',
            'password2': 'wikidika'
        })
        self.assertIs(form.is_valid(), False)
    
    def test_UserUpdateForm_valid(self):
        form = UserUpdateForm({
            'username' :'testuser',
            'email' : 'test@user.com',
            
        })
        self.assertIs(form.is_valid(), True)

    def test_UserUpdateForm_not_valid(self):
        form = UserUpdateForm({
            'email' : 'test@user.com',
        })
        self.assertIs(form.is_valid(), False)

    def test_ProfileUpdateForm_not_valid(self):
        form = ProfileUpdateForm()
        self.assertIs(form.is_valid(),False)

    def test_ProfileUpdateForm_valid(self):
        img = Image.open('test_img.jpeg')

        form = ProfileUpdateForm({'image':img})
        self.assertIs(form.is_valid(),True)