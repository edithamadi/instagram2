from django.shortcuts import render,redirect
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

def search_profile(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}" 

        return render(request, 'all-insta/search.html',{"message":message,"profiles": searched_profiles})
    else:
        message = "No results found"

        return render(request, 'all-insta/search.html',{"message":message})

    if request.method == 'POST':
        form = InstaForm(request.POST)

    if form.is_valid():
        print('valid')
    else:
        form = InstaForm()
    
    return render(request, 'all-insta/email.html', {"letterForm":form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.get_profile()
    image = Image.get_images()
    comments = Comment.get_comment()
    return render(request,'registration/profile.html',{"comments":comments,"image":image,"user":current_user,"profile":profile,})
    