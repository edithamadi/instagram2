from django import forms
from .models import Image,Profile
class InstaForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'comment']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo', 'bio', 'first_name')
        exclude = ['user', 'last_name']