from django.urls import path,include
from . import views

app_name = 'forms'
urlpatterns = [
    path('', views.home),
    path('home2/<int:id>/<int:age>/', views.home2, name='home2'),
    path('blog/<int:id>/', views.blog,{'foo':'bar'}),
    path('blog2/',include('polls2.inner')),
    path('abc/',include('polls2.urls')),
    path('articles/<int:year>/', views.article,name='art'),
    path('year/', views.redirect_to_year,name='year'),
    path('about/', views.about, name='about')
]