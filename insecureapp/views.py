from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from .models import User

# 1. Flaw SQL Injection 
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        cursor = connection.cursor()
        response = cursor.execute(f"SELECT * FROM insecureapp_user WHERE username = '{username}' AND password = '{password}'")

        if response:
            return HttpResponse("Login successful!")
        else:
            # 2. Flaw Security Logging and Monitoring Failure
            return HttpResponse("Invalid credentials!")
    
    return render(request, 'login.html')

# 3. Flaw Broken Access Control
def admin(request):
    return HttpResponse("Hello everybody! This view should be available only for admins.")

# 4. Flaw Identification and Authentication Failure
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create(username=username, password=password)
        return HttpResponse("User created!")

    return render(request, 'signup.html')



