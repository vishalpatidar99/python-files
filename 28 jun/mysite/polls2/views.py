from django.http import HttpResponse
from django.shortcuts import render
from .forms import*
from django.core.mail import send_mail
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