from django import forms
from .models import Image,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class InstaForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'comment']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo', 'bio', 'first_name')
        exclude = ['user', 'last_name']


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')