from django import forms
from .models import*

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'

class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = '__all__'

class InterviewUpdateForm(forms.ModelForm):
    class Meta:
        model = InterviewUpdate
        fields = '__all__'
        