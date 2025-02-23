from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blogs(models.Model):
    title= models.CharField(max_length=50)
    subtitle= models.CharField(blank=True, null=True, max_length=100)
    image= models.ImageField(upload_to="images")
    description= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE, default=1)