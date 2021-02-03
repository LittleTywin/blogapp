from django.test import TestCase
from django.urls import reverse, resolve
from django.test import Client

from users.views import login_view, logout_view, register_view, profile_view
from django.contrib.auth.models import User


class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user= User.objects.create(username='testuser')
        self.user.set_password('asdf5tgb')
        self.password='asdf5tgb'
        self.user.save()

    def tearDown(self):
        pass

    def test_home(self):
        response = self.client.get(reverse('blog:home'))
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'blog/base.html')
        self.assertTemplateUsed(response,'blog/home.html')


    def test_login_GET_logged_out(self):
        response = self.client.get(reverse('users:login'))
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'blog/base.html')
        self.assertTemplateUsed(response,'users/login.html')

    def test_login_GET_logged_in(self):
        
        self.client.force_login(user=self.user) ##problems when user has username
        response = self.client.get(reverse('users:login'))
       
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('blog:home'))

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('users:login'))
        self.assertRedirects(response, reverse('blog:home'))
        self.client.logout()
        
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code,200)


    def test_login_POST_logged_out_valid(self):
        username = self.user.username
        password = 'asdf5tgb'
        response = self.client.post(reverse('users:login'),{'username':username, 'password':password})
        self.assertRedirects(response,reverse('blog:home'))


    def test_login_POST_logged_out_invalid(self):
        response = self.client.post(reverse('users:login'),{'username':'aosd', 'password':'keiapl920'})
        
        self.assertEqual(response.status_code,200)
        
