from django.contrib import admin

# Register your models here.
@admin.register
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text','pub_date']

@admin.register
class dmin(admin.ModelAdmin):
    list_display = ['question_text','pub_date']