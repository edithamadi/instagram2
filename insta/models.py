from django.db import models

# Create your models here.
class Image(models.Model):
   image = models.ImageField(upload_to='images/')
   image_name = models.CharField(max_length=40)
   image_caption = models.TextField()
   likes = models.PositiveIntegerField(default=0)
   comments = models.CharField(max_length=200)
   profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
   