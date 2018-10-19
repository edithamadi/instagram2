from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=200)
    profile_photo = models.ImageField(upload_to='profile/')
   
    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


    @classmethod
    def get_user_profile(cls ,username):
        user = cls.objects.get(user = username)
        return user


    @classmethod
    def search_profile(cls , search_term):
        profiles = cls.objects.filter( first_name__icontains = search_term ) 
        return profiles

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def search_user(cls,search_term):
        profile = cls.objects.filter(first_name__icontains=search_term)
        return profile

    @classmethod
    def filter_by_id(cls,id):
        profile = Profile.objects.filter(user_id=id).all
        return profileComment
class Image(models.Model):
    user = models.ForeignKey(User ,on_delete = models.CASCADE )
    image = models.ImageField(upload_to='images/')
    posted_on = models.DateTimeField(auto_now_add=True)
    image_name = models.CharField(max_length=40)
    image_caption = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    #    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name 

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['posted_on']


    @classmethod
    def filter_by_id(cls,id):
        image = Image.objects.filter(user_id=id).all
        return image
    @classmethod
    def get_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def get_user_images(cls ,user):
        images = cls.objects.filter(user = user)
        return images


class Comment(models.Model):
    user = models.ForeignKey(User,null=True), 
    Profile = models.ForeignKey(Profile,null=True)
    comment_text = models.CharField(max_length=200,null=True)
    post = models.ForeignKey(Image,null=True)
    #    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text