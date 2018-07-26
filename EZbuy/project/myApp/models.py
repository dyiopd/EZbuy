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
    productPrice = models.FloatField()  # gprice = models.DecimalField(max_digits=5, decimal_places=2)
    productInformation = models.CharField(max_length=100)
    productCategory = models.IntegerField()
    productImage = models.ImageField(upload_to='img')
    isDelete = models.BooleanField(default=False)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)


class Comments(models.Model):
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
