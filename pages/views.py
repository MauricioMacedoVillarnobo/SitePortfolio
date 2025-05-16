from django.shortcuts import render

def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def tools_view(request):
    return render(request, 'pages/tools.html')

def contact_view(request):
    return render(request, 'pages/contact.html')
