from ctypes import addressof
from django.db import models
from django.contrib.auth.models import User


class userinfo(models.Model):

  ContactNumber = models.CharField(max_length=150)
  Address = models.CharField(max_length=150)
  Postcode = models.CharField(max_length=150)
  created_by = models.ForeignKey('auth.User', related_name='userimnfo', on_delete=models.CASCADE)
  date_created = models.DateField(auto_now_add=True)

