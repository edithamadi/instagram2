from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from .forms import NewsLetterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

    @login_required(login_url='/accounts/login/')

    def search_image(request):
        if 'image' in request.GET and request.GET["image"]:
            search_term = request.GET.get("image")
            searched_images = Image.search_image(search_term)
            message = f"{search_term}" 

            return render(request, 'all-insta/search.html',{"message":message,"images": searched_images})
        else:
            message = "No results found"

            return render(request, 'all-insta/search.html',{"message":message})

        if request.method == 'POST':
            form = NewsLetterForm(request.POST)

        if form.is_valid():
            print('valid')
        else:
            form = NewsLetterForm()
        
        return render(request, 'all-insta/email.html', {"letterForm":form})
    