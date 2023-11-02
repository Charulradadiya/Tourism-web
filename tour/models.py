from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tour(models.Model):
    image = models.ImageField(upload_to='tour/static/images/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=10)
    url=models.URLField(blank=False)

class Reviews(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour,on_delete=models.CASCADE)