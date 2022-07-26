from django.urls import path, register_converter, re_path
from . import views, converters
register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('articles/2003/',views.articles_2003),
    # path('articles/<int:year>/', views.year_archives),
    path('articles/<int:year>/<int:month>/', views.month_archives),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.articles_detail),
    # path('articles/<yyyy:year>/', views.year_archives),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archives),
    path('', views.blogform),
    path('blogform/', views.blogform),
    path('view1/', views.myview, name='view1'),
    path('userview/', views.UserView.as_view(), name='view2'),
    path('success/', views.success, name='success'),
    # path('publisher1/', views.PublisherCreateView.as_view(), name='publisher1'),
    # path('publisher2/<int:pk>/',views.PublisherDetailView.as_view(), name='publisher2'),
    path('publisher1/',views.PublisherRegisterView.as_view(), name='publisherregister'),
    path('publisher2/',views.PublishersListView.as_view(), name='publisherlist'),
]