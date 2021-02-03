from django.test import SimpleTestCase
from django.urls import reverse, resolve

from users.views import login_view, logout_view, register_view, profile_view

class TestUrls(SimpleTestCase):

    def test_login_url_resolve(self):
        url = reverse('users:login')
        assert(
            resolve(url).func == login_view
        )
    
    def test_logout_url_resolve(self):
        url = reverse('users:logout')
        assert(
            resolve(url).func == logout_view
        )
    
    def test_register_url_resolve(self):
        url = reverse('users:register')
        assert(
            resolve(url).func == register_view
        )
    
    def test_profile_url_resolve(self):
        url = reverse('users:profile')
        assert(
            resolve(url).func == profile_view
        )