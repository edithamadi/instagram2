from django.shortcuts import render,redirect ,get_object_or_404
from django.http import HttpResponse
from .models import Image,Profile
from .forms import InstaForm,ProfileForm,SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from .tokens import account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import login, authenticate
from django.template.loader import render_to_string

# Create your views here.

  
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
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

# @login_required(login_url='/accounts/login/')
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



# @login_required(login_url='/accounts/login/')
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
  