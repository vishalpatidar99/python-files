from django.urls import path
from forms import views

urlpatterns=[
    path('archive/',views.archiev),
    path('about/',views.about),
]