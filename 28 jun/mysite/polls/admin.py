from django.contrib import admin
from .models import *
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets =[
        (None, {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question{_text']

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Person)
admin.site.register(Toppings)
admin.site.register(Pizzas)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Students)
admin.site.register(Coaching)
admin.site.register(Manufacture)
admin.site.register(Cars)
admin.site.register(Hospital_2)
admin.site.register(Doctor_2)
admin.site.register(Patient_2)
admin.site.register(Blog)
admin.site.register(StudentNew1)
admin.site.register(Studentnew2)
admin .site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Person2)
admin.site.register(MyPerson)
admin.site.register(MyPerson2)
admin.site.register(MyPerson3)
admin.site.register(Student2)
admin.site.register(Student3)
admin.site.register(MoonLandings)   
admin.site.register(Registration)
admin.site.register(Practice)
admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Filing3)
admin.site.register(Practice2)
admin.site.register(Author)
admin.site.register(Blog2)
admin.site.register(Entry)