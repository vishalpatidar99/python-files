from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title','birth_date']
        labels = {'name':_('Writer'),
        'title':'Title',
        'birth_date':'Birth Date'}
        widgets =  {'name':forms.TextInput(attrs={'placeholder':'Enter Your full name here'}),
        'title':forms.Select,
        'birth_date':forms.SelectDateWidget
        }
        error_messages = {
            'name': {
                'required': _("Andha hai kya")
            }
        }
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        # exclude = ['name']    