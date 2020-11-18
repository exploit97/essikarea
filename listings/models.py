from django.db import models
from realtors.models import Profile
from datetime import datetime
from PIL import Image


class Ville(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.name
    

class Arrondissement(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name
class District(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    arrondissement = models.ForeignKey(Arrondissement, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name

class Propriete(models.Model):
    realtor=models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    ville=models.CharField(max_length=200,null = True,blank=True)
    arrondissement=models.CharField(max_length=200,null = True,blank=True)
    district=models.CharField(max_length=200,null = True,blank=True)
    type_immo = models.CharField(max_length=200,null = True,blank=True)
    gender = models.CharField(max_length=200,null=True,blank=True)
    price=models.IntegerField()
    description=models.TextField()
    list_date=models.DateTimeField(default=datetime.now,blank=True)
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/',default='default.png')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,null=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,null=True)
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,null=True)
    photo_4=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,null=True)
    photo_5=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,null=True)
    photo_6=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,null=True)
    is_published=models.BooleanField(default=True)
    bedroom=models.IntegerField(blank=True,null=True)
    room = models.IntegerField(blank=True,null=True)
    bathroom=models.IntegerField(blank=True,null=True)
    garage=models.IntegerField(blank=True,null=True)
    kitchen = models.IntegerField( blank=True,null=True)
    veranda = models.IntegerField(blank=True,null=True)
    sqft=models.IntegerField(blank=True,null=True)
    lot_size=models.DecimalField(max_digits=5,decimal_places=1,blank=True,null=True)


    def __str__(self):
        return self.title





    

   
