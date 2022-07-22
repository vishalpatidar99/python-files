from django import forms
from .models import *
from polls2.models import*

class FileUploadForm(forms.Form):
    title = forms.CharField(label='Enter Title', max_length=35)
    file = forms.FileField()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class FileFieldForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
    