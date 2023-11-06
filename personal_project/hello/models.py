from django.db import models
from django.conf import settings



class Members(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    nicknames = models.CharField(max_length=20)
    telnos = models.CharField(max_length=20)
    dates = models.CharField(max_length=20)

def __str__(self):
    return self.handnos

class Letter(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    mess_reco = models.CharField(max_length=200)
    mess_id = models.CharField(max_length=200)
    mess_titles = models.CharField(max_length=200)
    mess_dates = models.CharField(max_length=200)
    dates = models.CharField(max_length=20)
    url = models.CharField(max_length=200)

def __str__(self):
    return self.username


class MyModel(models.Model):
    upload_file = models.ImageField(upload_to='uploads/')


    class Snack(models.Model):
        name = models.CharField(max_length=100)
        
