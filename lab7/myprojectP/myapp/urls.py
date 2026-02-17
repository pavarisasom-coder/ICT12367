from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('form/', views.form, name='form'),
    path('contact/', views.contact, name='contact')
]