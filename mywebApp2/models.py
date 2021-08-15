from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    Name = models.CharField(max_length=200,blank=False,default='')
    age =models.CharField(max_length=200,blank=False,default='')
    key = models.CharField(max_length=200,blank=False,default='')
    gender =models.CharField(max_length=200,blank=False,default='')

class StudentDetails1(models.Model):
    Name = models.CharField(max_length=200,blank=False,default='')
    age =models.CharField(max_length=200,blank=False,default='')
    key = models.CharField(max_length=200,blank=False,default='')
    gender =models.CharField(max_length=200,blank=False,default='')
    