from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from student_app.EmailBackEnd import EmailBackEnd
from student_app.models import CustomUser 
from student_system import settings

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def showDemoPage(request):
    return render(request,"demo.html")

def ShowLoginPage(request):
    return render(request,"login_page.html")

      

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")


def Testurl(request):
    return HttpResponse("Ok")

def signup_admin(request):
    return render(request,"signup_admin_page.html")

def signup_student(request):
    return render(request,"signup_student_page.html")

@api_view(['POST'])
def student_signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if CustomUser.objects.filter(email=email).exists():
            return Response({"error": "Email already exists. Please use a different email."}, status=status.HTTP_400_BAD_REQUEST)
        elif CustomUser.objects.filter(username=username).exists():
            return Response({"error": "Username already exists. Please choose a different username."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                validate_email(email)
            except ValidationError:
                return Response({"error": "Invalid email format. Please provide a valid email."}, status=status.HTTP_400_BAD_REQUEST)
            
            user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name,
                                             first_name=first_name, user_type=3)
            user.save()
            return Response({"message": "Successfully signed up."}, status=status.HTTP_201_CREATED)
    else:
        return Response({"error": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
 
@api_view(['POST'])
def login_check(request):
    if request.method != "POST":
        return Response({"error": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            return Response({"error": "Please enter email and password."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            loginuser = EmailBackEnd.authenticate(request, email=email, password=password)
            if loginuser is not None:
                login(request, loginuser)
                if loginuser.user_type == 1:
                    return Response({"message": "Admin logged in successfully.", "redirect_url": "/admin_home"}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Student logged in successfully.", "redirect_url": "/student_home"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid Login Details"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)

