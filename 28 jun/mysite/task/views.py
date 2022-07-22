from django.urls import reverse
import datetime
from django.http import FileResponse, HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_list_or_404, redirect, render
from polls2.models import *
from django.template import loader
from django.shortcuts import get_object_or_404
from .forms import*
from .somewhere import handle_uploaded_file
from django.views.generic.edit import FormView

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
    return JsonResponse()

def my_view8(request):
    q ={'a':202}
    return JsonResponse(data=q, safe=False)

def my_view9(request):
    return FileResponse(open('media/furniture.png', 'rb'))

def fileupload(request):
    if request.method=='POST':
        form = FileUploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File Uploaded Successfully...")
    else:
        form = FileUploadForm()
    return render(request, 'file.html', {'form':form})

def fileupload2(request):
    if request.method=='POST':
        form = UserForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task:file2'))
    else:
        form = UserForm()
    return render(request, 'file.html', {'form':form})

class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = 'file3.html'
    success_url = 'polls:results'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
