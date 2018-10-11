from django.shortcuts import render,redirect ,get_object_or_404
from django.http import HttpResponse
from .models import Image,Profile
from .forms import InstaForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET["search"]
        searched_profiles = Profile.search_profile(search_term)
        print(searched_profiles)
        message = f"{search_term}" 

        return render(request, 'all-insta/search.html',{"message":message,"profiles": searched_profiles})
    else:
        message = "No results found"

        return render(request, 'all-insta/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def profile(request , user_username = None):

    if user_username == None:
        user = request.user 
    else:
        user = get_object_or_404(User ,username = user_username)

    images = Image.get_user_images(user).order_by('-id')[::-1]
    profile = Profile.get_user_profile(user)

    data = {
        'images' : images ,
        'profile' : profile , 
        
    }

    return render(request,'registration/profile.html', data )



@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':
        user_form = InstaForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = InstaForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })