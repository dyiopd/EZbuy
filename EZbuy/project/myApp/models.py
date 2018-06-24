from django.db import models

# Create your models here.

class Users(models.Model):
    UserID = models.CharField(max_length=20)
    # models.IntegerField()
    # models.BooleanField()
