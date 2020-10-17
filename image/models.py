from django.db import models
import datetime as dt

class Profile(models.Model):
  profile_pic = models.ImageField()
  bio = models.TextField()
  
  def __str__(self):
    return self.bio
  
class Image(models.Model):
  image = models.ImageField()
  image_name = models.CharField(max_length=150)
  image_caption = models.TextField()
  likes = models.IntegerField()
  comments = models.TextField()
  post_date = models.DateTimeField(auto_now_add=True)
  profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
  
  def __str__(self):
    return self.image_name
  
