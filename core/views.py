from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'core/landing_page.html')

def register_organizer(request):

    return render(request, 'core/register_organizer.html')

def register_voter(request):

    return render(request, 'core/register_voter.html')

def login(request):

    return render(request, 'core/login.html')

def signup_organizer(request):

    return render(request, 'core/signup.html')

def signup_voter(request):

    return render(request, 'core/signup.html')