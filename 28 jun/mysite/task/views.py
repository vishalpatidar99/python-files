import datetime
from django.http import HttpResponse, Http404, HttpResponseNotAllowed, HttpResponseNotModified, HttpResponsePermanentRedirect
from django.shortcuts import get_list_or_404, redirect, render
from polls2.models import *
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<h1>It is Now %s<h1>"%now
    request.GET.copy().appendlist('a','25')
    print(request.GET)
    return HttpResponse(html)

async def my_view(request):
    try:
        b = Blog.objects.get(pk=111)
    except Blog.DoesNotExist:
        raise Http404('Blog does not exist')
    return HttpResponse("Great!")

def my_view2(request):
    t = loader.get_template('index.html')
    c = {'foo':'bar'}
    return HttpResponse (t.render(c, request))

def my_view3(request):
    obj = Blog.objects.get(id=5)
    return redirect('task:time')    

def my_view4(request):
    obj = get_object_or_404(Blog, pk=3)
    return HttpResponse(obj.tagline)
    
def my_view5(request):
    try:
        obj = Blog.objects.get(pk=23)
    except Blog.DoesNotExist:
        return render(request, '404.html')
    return HttpResponse(obj.tagline)

def my_view6(request):
    objects = get_list_or_404(Blog, name__contains='Blog')
    return HttpResponse(objects)

def my_view7(request):
    return HttpResponseNotAllowed(request.GET)