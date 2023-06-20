from django.shortcuts import render

def register(request):
    return render(request, 'register.html')

def user_creation(request):
    return render(request, 'user_creation.html')

def portfolio_creation(request):
    return render(request, 'portfolio_creation.html')

def achievement_upload(request):
    return render(request, 'achievement_upload.html')

def profile(request):
    return render(request, 'profile.html')

def quniob(request):
    return render(request, 'quniob.html')