from django import forms
from django.forms import ModelForm
from .models import *
from django import forms
# class NameForm(forms.Form):
#     your_name = forms.CharField(label="Name",max_length=100)
    
# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'tagline']
