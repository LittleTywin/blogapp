from django.test import SimpleTestCase
from django.urls import reverse, resolve

from blog.views import home

class TestUrls(SimpleTestCase):

    def test_home_url_resolve(self):
        url = reverse('blog:home')
        assert(
            resolve(url).func == home
        )