from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
# Create your views here.
def home(request):
    if request.method=="POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            birth_date = form.cleaned_data['birth_date']
            p = Author(name=name,title=title,birth_date=birth_date)
            p.save()
            return render(request,'home.html',{'output':'Data Submited Successfully...'})
        else:
            return render(request,'home.html',{'output':'Data is Invalid'})
    else:    
        form = AuthorForm()
        return render(request, 'home.html',{'form':form,'output':''})

def home2(request,id,age):
    # print(id)
    # print(age)
    return HttpResponse("This is Home2")