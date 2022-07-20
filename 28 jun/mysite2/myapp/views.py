from django.shortcuts import render
from .models import*
from .forms import*
# Create your views here.
def form(request):
    if request.method=="POST":
        fm = CandidateForm(request.POST)
        output=''
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            phone1 = fm.cleaned_data['phone1']
            phone2 = fm.cleaned_data['phone2']
            address = fm.cleaned_data['address']
            gender = fm.cleaned_data['gender']
            profile = fm.cleaned_data['profile']
            source = fm.cleaned_data['source']
            f = Candidate(name=name, email=email,phone1=phone1,phone2=phone2,address=address,gender=gender,profile=profile,source=source)
            f.save()
            output = 'Form Was Submitted Successfully...'
        return render(request, 'form.html', {'form':fm,'output':output})

    else:
        fm = CandidateForm()
        return render(request, 'form.html',{'form':fm,'output':''} )
            