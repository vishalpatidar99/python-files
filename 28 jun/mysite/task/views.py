import datetime
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from polls2.models import *
from django.template import loader
# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<h1>It is Now %s<h1>"%now
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
    return HttpResponse (t.render(c, request), content_type='application/xhtml+xml')

def my_view3(request):
    obj = Blog.objects.get(id=5)
    return redirect("task:current_datetime")