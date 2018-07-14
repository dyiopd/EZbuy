import os
import unittest

from django.test import TestCase
# Create your tests here.
import django


def check_django_environment(default_settings):
    # Environment setup for Django project files:
    os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if not os.environ.get('DJANGO_SETTINGS_MODULE'):
        # Don't override settings if it is specified.
        os.environ['DJANGO_SETTINGS_MODULE'] = default_settings
        from django.conf import settings

        return getattr(settings, 'DEBUG', None)


check_django_environment('project.settings')

django.setup()
from django.contrib.auth.models import User
from django.test import Client


class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username='test1', email="123@163.com", password="123")

    def testUser(self):
        u = User.objects.get(username='test1')
        self.assertEqual(u.username, 'test1')
        self.assertEqual(u.email, '123@163.com')

    def testIndex(self):
        c = Client()
        response = c.post('/index/')
        self.assertEqual(response.status_code, 200)

    def testSignin(self):
        c = Client()
        c.login(username='test', password='123')
        response = c.post('/signin/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self, c.login(username='test', password='123'))

    def testSignup(self):
        c = Client()
        response = c.post('/signup/')
        self.assertEqual(response.status_code, 200)

    def testMobiles(self):
        c = Client()
        response = c.post('/mobiles/0/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
