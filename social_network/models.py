from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
     city = models.CharField(max_length=100, blank=True)
     etat = models.CharField(max_length=100, blank=True)
     email = models.EmailField(unique=True)
    
     def __str__(self):
            return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    post_message=models.CharField(max_length=2000)
    date=models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name="author")