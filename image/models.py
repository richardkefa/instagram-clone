from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.urls import reverse
  
class Image(models.Model):
  image = models.ImageField(upload_to = 'images/')
  image_name = models.CharField(max_length=150)
  image_caption = models.TextField(blank=True)
  likes = models.IntegerField(default=0)
  post_date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE,default='1')
  
  def __str__(self):
    return self.image_name
  
  def save_image(self):
    return self.save()
  
  def del_image(self):
    return self.delete()
  
  @classmethod
  def all_images(cls):
    all_images = cls.objects.all()
    return all_images
  
  
  @classmethod
  def image_details(cls,id):
    image_details = cls.objects.filter(pk=id)
    return image_details
  
  def get_absolute_url(self):
    return reverse('one_image',kwargs={'image_id':self.pk}) 
      
  
class Comment(models.Model):
  comment = models.CharField(max_length=3000)
  image = models.ForeignKey(Image,on_delete=models.CASCADE)

  def __str__(self):
    return self.comment
  
  @classmethod
  def image_comments(cls,id):
    comments = cls.objects.filter(image=id)
    
    return comments