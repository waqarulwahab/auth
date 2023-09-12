from django.shortcuts import render

# Create your views here.

def signin_page(request):
    return render(request , 'auth_app\signin.html')

def signup_page(request):
    return render(request , 'auth_app\signup.html')