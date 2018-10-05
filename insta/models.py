from django.db import models

# Create your models here.
class Profile(models.Model):
   username = models.ForeignKey(User, on_delete=models.CASCADE)
   bio = models.CharField(max_length=200)
   profile_photo = models.ImageField(
       upload_to='profile/')

   def __str__(self):
       return self.username

   def save_profile(self):
       self.save()

   def delete_profile(self):
       self.delete()

       @classmethod
       def search_by_username(cls,search_term):
           insta = cls.objects.filter(title__icontains=search_term)
           return insta

class Image(models.Model):
   image = models.ImageField(upload_to='images/')
   image_name = models.CharField(max_length=40)
   image_caption = models.TextField()
   likes = models.PositiveIntegerField(default=0)
   comments = models.CharField(max_length=200)
   profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
   def __str__(self):
       return self.image_name 

   def save_image(self):
       self.save()

   def delete_image(self):
       self.delete()

   

