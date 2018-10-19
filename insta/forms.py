from django import forms
from .models import Image,Profile,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class InstaForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['posted_on','likes', 'comment']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        
        widgets = {
            'bio': forms.TextInput(attrs={'placeholder': 'Bio'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Name'}),
            }
        exclude = ['user', 'last_name']

class UserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
