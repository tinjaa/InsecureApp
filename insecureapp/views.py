from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from .models import User
#import logging
#logger = logging.getLogger(__name__)
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.password_validation import validate_password
#from django.core.exceptions import ValidationError
#from django.contrib.auth.models import User
#from django.contrib.auth.hashers import make_password


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        cursor = connection.cursor()

        # 1. Flaw SQL Injection 
        response = cursor.execute(f"SELECT * FROM insecureapp_user WHERE username = '{username}' AND password = '{password}'")
        # response = cursor.execute("SELECT * FROM insecureapp_user WHERE username = %s AND password = %s", [username, password])
        # response = User.objects.filter(username=username, password=password).first()

        if response:
            return HttpResponse("Login successful!")
        else:
            # 2. Flaw Security Logging and Monitoring Failure
            # logger.warning(f"Failed login attempt for username: {username}")
            return HttpResponse("Invalid credentials!")
    
    return render(request, 'login.html')

# 3. Flaw Broken Access Control
#@login_required
def admin(request):
    #if not request.user.admin:
    #    return HttpResponse("Access Denied", status=403)
    return HttpResponse("Hello everybody! This view should be available only for admins.")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #hashedpassword = make_password(password)
        #User.objects.create(username=username,password=password)

        # 4. Flaw Identification and Authentication Failure
        User.objects.create(username=username, password=password)
        #return HttpResponse("User created!")

        #try:
        #    validate_password(password)
        #    User.objects.create(username=username, password=password)
        #    return HttpResponse("User created!")
        #except ValidationError as e:
        #    return HttpResponse(f"Too weak password: {e}", status=400)

    return render(request, 'signup.html')



