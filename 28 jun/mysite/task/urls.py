from django.urls import path
from . import views

app_name = 'task'
urlpatterns = [
    path('time/', views.current_datetime, name='time'),
    path('myview/', views.my_view, name='myview'),
    path('myview2/', views.my_view2, name='myview2'),
    path('myview3/', views.my_view3, name='myview3'),
]   