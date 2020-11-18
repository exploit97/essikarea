from django.db import models
from datetime import datetime
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(default='default.png', upload_to='photos/%Y/%m/%d/')
    description=models.CharField(max_length=255, blank=True, null=True)
    is_mvp=models.BooleanField(default=False)
    hire_date=models.DateTimeField(default=datetime.now,blank=True)
    website_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)
    twitter_url = models.CharField(max_length=255, blank=True, null=True)
    linkedin_url = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)
        if img.height >100 or img.width>100:
            output_size = (100,100)
            img.thumbnail(output_size)
            img.save(self.photo.path)


class Demande(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)


    def __str__(self):
        return self.profile.user.username