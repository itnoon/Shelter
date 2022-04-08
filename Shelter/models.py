import email
from unicodedata import name
from django.db import models
class Contact(models.Model):
  name=models.CharField(max_length=100,null=True)
  phone=models.CharField(max_length=100,null=True)
  email=models.CharField(max_length=100,null=True)
  def __str__(self):
      return self.name
class Register(models.Model):
  email=models.CharField(max_length=100,null=True)
  password=models.CharField(max_length=100,null=True)
  repeatpassword=models.CharField(max_length=100,null=True)
  def __str__(self):
      return self.email
class About(models.Model):
  username=models.CharField(max_length=100,null=True)
  password=models.CharField(max_length=100,null=True)
  def __str__(self):
      return self.username
class Login(models.Model):
  name=models.CharField(max_length=100,null=True)
  phone=models.CharField(max_length=100,null=True)
  email=models.CharField(max_length=100,null=True)
  comments=models.CharField(max_length=500,null=True)
  def __str__(self):
      return self.name