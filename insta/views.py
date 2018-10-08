from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from .forms import InstaForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    images=Image.objects.all()

    return render(request,'welcome.html',{'images':images})
    
@login_required(login_url='/accounts/login/')
def new_img(request):
    current_user = request.user
    if request.method == 'POST':
        form = InstaForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('welcome')

    else:
        form = InstaForm()
    return render(request, 'new_img.html', {"form": form})
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
    