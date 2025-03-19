from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),      # <== Make sure this line exists!
    path('courses/', views.courses, name='courses'),
    path('contact/', views.contact, name='contact'),
]