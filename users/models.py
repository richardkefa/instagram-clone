from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profiles(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  bio = models.TextField()
  profile_pic = models.ImageField(default='default.jpg',upload_to='profile_pic/')
  
  def __str__(self):
    return f'{self.user.username} Profiles'
  
  # def save(self):
  #   super().save()
  #   img = Image.open(self.profile_pic.path)
  #   rgb_im = img.convert('RGB')
  #   if rgb_im.height > 300 or rgb_im.width > 300:
  #     output_size = (300,300)
  #     rgb_im.thumbnail(output_size)
  #     rgb_im.save(self.profile_pic.path)