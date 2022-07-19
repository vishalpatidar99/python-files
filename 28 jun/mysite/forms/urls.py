from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home2/<int:id>/<int:age>/', views.home2, name='home2')
]