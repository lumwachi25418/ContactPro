from django.db import models

class Contact(models.Model):
    firstname=models.CharField(max_length=50,)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=200,unique=True,blank=True,null=True)
    phonenumber=models.IntegerField(unique=True)
    address=models.CharField(null=True,blank=True)
    birthday=models.DateField(blank=True,null=True)
