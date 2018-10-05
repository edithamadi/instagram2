from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

    def search_image(request):
        if 'image' in request.GET and request.GET["image"]:
            search_term = request.GET.get("image")
            searched_images = Image.search_image(search_term)
            message = f"{search_term}" 

            return render(request, 'all-insta/search.html',{"message":message,"images": searched_images})
        else:
            message = "No results found"

            return render(request, 'all-insta/search.html',{"message":message})