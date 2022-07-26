from django.urls import path
from . import views

app_name = 'task'
urlpatterns = [
    path('time/', views.current_datetime, name='time'),
    path('myview/', views.my_view, name='myview'),
    path('myview2/', views.my_view2, name='myview2'),
    path('myview3/', views.my_view3, name='myview3'),
    path('myview4/', views.my_view4, name='myview4'),
    path('myview5/', views.my_view5, name='myview5'),
    path('myview6/', views.my_view6, name='myview6'),
    path('myview7/', views.my_view7, name='myview7'),
    path('myview8/', views.my_view8, name='myview8'),
    path('myview9/', views.my_view9, name='myview9'),
    path('file/', views.fileupload, name='file'),
    path('file2/', views.fileupload2, name='file2'),
    path('file3/', views.FileFieldFormView.as_view(), name='file3'),
    path('view1/', views.My_View.as_view(), name='view1'),
]   