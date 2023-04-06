from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class Categury (models.Model):
    name =models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book (models.Model):
    state_book=[
     ('available','available'),
     ('rental','rental'),
     ('sold','sold'),
     ]
    titel =models.CharField(max_length=50)    
    author =models.CharField(max_length=50)  
    photo_book =models.ImageField(upload_to='media\photos',null=True,blank=True) 
    photo_aythor =models.ImageField(upload_to='photos/',default='static/image/p1'  ,null=True,blank=True) 
    pages =models.IntegerField(null=True,blank=True)  
    price=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    total_rental=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    reyal_price_day=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    retal_period=models.IntegerField(null=True,blank=True)  
    active=models.BooleanField(default=True)
    status=models.CharField(max_length=50,choices=state_book,null=True,blank=True)
    categury=models.ForeignKey(Categury,on_delete=models.PROTECT,null=True,blank=True)
     
    def __str__(self):
        return self.titel