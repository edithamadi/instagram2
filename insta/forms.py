from django import forms
from .models import Image
class InstaForm(forms.ModelForm):
    class Meta:
        model=Image
        exclude = ['likes', 'comment']
