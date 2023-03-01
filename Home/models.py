from django.db import models

# Create your models here.
class user(models.Model):
    Userid = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
class Entry(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=50)
    SURNAME = models.CharField(max_length=50)
    USERID = models.CharField(max_length=50)
