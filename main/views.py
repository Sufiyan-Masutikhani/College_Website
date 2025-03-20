from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def courses(request):
    courses_data = [
        {'name': 'Computer Science', 'description': 'Learn algorithms, programming, and more.', 'duration': '4 Years'},
        {'name': 'Mechanical Engineering', 'description': 'Design machines and innovate.', 'duration': '4 Years'},
        {'name': 'Civil Engineering', 'description': 'Build infrastructure and cities.', 'duration': '4 Years'},
    ]
    return render(request, 'main/courses.html', {'courses': courses_data})

def contact(request):
    return render(request, 'main/contact.html')