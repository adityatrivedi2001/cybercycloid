from django.urls import path

from . import views

urlpatterns =[
	path('', views.homepage , name='homepage'),
    path('services/', views.services , name='services'),
    path('about/', views.about , name='about'),
    path('contact', views.contact12 , name = 'contact12'),
    path('contact2', views.contact1 , name = 'contact1'),
]