from django.db import models

# Create your models here.
class Doctor(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=1000,default='')
	fname = models.CharField(max_length=1000,default='')
	lname = models.CharField(max_length=1000,default='')
	email = models.EmailField(max_length=255,unique=True)
	password = models.CharField(max_length=1000,default='')
	address = models.CharField(max_length=1000,default='')
	photo = models.ImageField(upload_to = 'events/',blank = True)

class Patient(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=1000,default='')
	fname = models.CharField(max_length=1000,default='')
	lname = models.CharField(max_length=1000,default='')
	email = models.EmailField(max_length=255,unique=True)
	password = models.CharField(max_length=1000,default='')
	address = models.CharField(max_length=1000,default='')
	photo = models.ImageField(upload_to = 'events/',blank = True)
