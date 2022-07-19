from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Candidate)
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Qualification)
admin.site.register(InterviewUpdate)