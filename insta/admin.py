from django.contrib import admin
# Register your models here.
from .models import Image,Profile

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('comments',)


admin.site.register(Image)
admin.site.register(Profile)
