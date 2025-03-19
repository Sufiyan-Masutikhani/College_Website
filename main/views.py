from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def courses(request):
    return render(request, 'main/courses.html')

def contact(request):
    return render(request, 'main/contact.html')