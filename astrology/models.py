from pyexpat import model
from unicodedata import category
from django.db import models

# Create your models here.

class Blog(models.Model):
    category_name =models.CharField(null=False,max_length=100)
    blog=models.CharField(null=False,max_length=1000)
    image=models.ImageField(upload_to='imagesb/',)

class Catagory(models.Model):
    category_name =models.ForeignKey(Blog, on_delete=models.CASCADE)

