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
from django.http import HttpRequest

from myApp.models import Products, Comments
from myApp.views import mobiles

from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore


class UserTestCase(TestCase):

    def setUp(self):
        u = User.objects.create_user(username='test1', email="123@163.com", password="123")
        Products.objects.create(productName='aa', productPrice=12, productInformation='aa', productCategory=1,
                                productImage='img/IMG_0400_hLhRP8Q.JPG', isDelete=False, buyer=u)
        Products.objects.create(productName='ele', productPrice=12, productInformation='ele', productCategory=2,
                                productImage='img/IMG_0400_hLhRP8Q.JPG', isDelete=False, buyer=u)
        Products.objects.create(productName='bike', productPrice=12, productInformation='bike', productCategory=3,
                                productImage='img/IMG_0400_hLhRP8Q.JPG', isDelete=False, buyer=u)
        Products.objects.create(productName='book', productPrice=12, productInformation='book', productCategory=4,
                                productImage='img/IMG_0400_hLhRP8Q.JPG', isDelete=False, buyer=u)
        Comments.objects.create(description='Nice', owner=u)

    def testUser(self):
        u = User.objects.get(username='test1')
        self.assertEqual(u.username, 'test1')
        self.assertEqual(u.email, '123@163.com')

    def testProducts(self):
        p = Products.objects.get(productName='aa')
        self.assertEqual(p.productName, 'aa')
        self.assertEqual(p.productPrice, 12)
        self.assertEqual(p.productInformation, 'aa')
        self.assertEqual(p.productCategory, 1)
        self.assertEqual(p.productImage, 'img/IMG_0400_hLhRP8Q.JPG')

    def testComments(self):
        c = Comments.objects.get(description='Nice')
        self.assertEqual(c.description, 'Nice')

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
        response = c.post('/mobiles/1/0/')
        productList = Products.objects.filter(productCategory='1')
        self.assertEqual(response.status_code, 200)
        for product in productList:
            self.assertEqual(product.productCategory, 1)

    def testElectronics(self):
        c = Client()
        response = c.post('/electronics/1/0/')
        productList = Products.objects.filter(productCategory='2')
        self.assertEqual(response.status_code, 200)
        for product in productList:
            self.assertEqual(product.productCategory, 2)

    def testBikes(self):
        c = Client()
        response = c.post('/bikes/1/0/')
        productList = Products.objects.filter(productCategory='3')
        self.assertEqual(response.status_code, 200)
        for product in productList:
            self.assertEqual(product.productCategory, 3)

    def testBooks(self):
        c = Client()
        productList = Products.objects.filter(productCategory='4')
        response = c.post('/books/1/0/')
        self.assertEqual(response.status_code, 200)
        for product in productList:
            self.assertEqual(product.productCategory, 4)


if __name__ == '__main__':
    unittest.main()
