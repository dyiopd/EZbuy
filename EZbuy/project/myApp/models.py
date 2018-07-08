from django.db import models

from django.contrib.auth.models import User


# Create your models here.

# class Users(models.Model):
#     username = models.IntegerField(unique=True)
#     userpwd = models.CharField(max_length=50)
#     useremail = models.CharField(max_length=100)
#     usertel = models.IntegerField(null=True,blank=True)
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return self.username
#
#
# class Sellers(Users):
#     postid = models.IntegerField()
#
#
# class Customers(Users):
#     pass
#
#
class Products(models.Model):
    productName = models.CharField(max_length=40)
    productInformation = models.CharField(max_length=100)
    productCategory = models.IntegerField()
    productImage = models.ImageField(upload_to='img')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)