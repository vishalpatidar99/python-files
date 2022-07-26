from django.http import HttpResponse
from django.shortcuts import render
from .forms import*
from django.views.generic import*
from django.views.generic.edit import*
# Create your views here.
def articles_2003(request):
    return HttpResponse("This is articles 2003")

def year_archives(request,**kwargs):
    return HttpResponse("This is year_archives")

def month_archives(request,**kwargs):
    return HttpResponse("This is month_archives")

def articles_detail(request,**kwargs):
    return HttpResponse("This is articles_detail")

# def get_name(request):
#     if request.method == "POST":
#         form  = NameForm(request.POST)
#         if form.is_valid():
#             return HttpResponse('Thanks')
#     else:
#         form = NameForm()
#     return render(request, 'registration.html', {'form':form})

# def get_mail(request):
#     form = ContactForm()
    # if request.method=="POST":
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         subject = form.cleaned_data['subject']
    #         message = form.cleaned_data['message']
    #         sender = form.cleaned_data['sender']
    #         cc_myself = form.cleaned_data['cc_myself']
    #         recipients = ['info@example.com']
    #         if cc_myself:
    #             recipients.append(sender)

    #         send_mail(subject,message,sender,recipients)
    #         return HttpResponse("Thanks")
    # return render(request, 'registration.html', {'form':form})

def blogform(request):
    if request.method=="GET":
        b=Blog.objects.get(id=1)
        form = BlogForm(instance=b)
        return render(request, 'registration.html', {'form':form})
    else:
        return HttpResponse("Thanks")
        
def myview(request):
    form = BookForm()
    if request.method=='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            p = Book5(title=title,date=date)
            p.save()    
            return HttpResponse('Success')
    else:
        form = BookForm()
    return render(request,'bookform.html',{'form':form})

class UserView(CreateView):
    model = User
    fields = '__all__'
    success_url = '/polls2/success/'

def success(request):
    return HttpResponse('Successfull')

# class PublisherCreateView(CreateView):
#     queryset = Publisher.objects.all()
#     context_object_name ={'objects_list':queryset}
#     model = Publisher
#     fields = '__all__'
#     success_url = '/polls2/success/'

# class PublisherDetailView(DetailView):
#     model = Publisher
#     fields = '__all__'

class PublisherRegisterView(View):
    def get(self, request):
        form = PublisherForm()
        return render(request,'publisher_form.html',{'form':form})

    def post(self, request):
        form = PublisherForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            Publisher.objects.create(name=name,address=address,city=city,state=state)
            return render(request,'publisher_form.html',{'form':form})

class PublishersListView(View):
    def get(self, request):
        data = Publisher.objects.all().order_by('id')
        return render(request, 'publisher_details.html',{'data':data})