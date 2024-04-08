from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from student_app.EmailBackEnd import EmailBackEnd
from student_app.models import CustomUser, Courses, SessionYearModel
from student_system import settings


def showDemoPage(request):
    return render(request,"demo.html")

def ShowLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if email and password are provided
        if not email or not password:
            messages.error(request, "Please provide both email and password.")
            return HttpResponseRedirect("/")
        else:
            user = EmailBackEnd.authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == "1":
                    return HttpResponseRedirect('/admin_home')
                else:
                    return HttpResponseRedirect(reverse("student_home"))
            else:
                messages.error(request, "Invalid Login Details")
                return HttpResponseRedirect("/") 
            

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")


def Testurl(request):
    return HttpResponse("Ok")

# def signup_admin(request):
#     return render(request,"signup_admin_page.html")

def signup_student(request):
    courses=Courses.objects.all()
    session_years=SessionYearModel.object.all()
    return render(request,"signup_student_page.html",{"courses":courses,"session_years":session_years})



def do_admin_signup(request):
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")

    try:
        user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=1)
        user.save()
        messages.success(request,"Successfully Created Admin")
        return HttpResponseRedirect(reverse("show_login"))
    except:
        messages.error(request,"Failed to Create Admin")
        return HttpResponseRedirect(reverse("show_login"))


def do_signup_student(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Check if the email or username already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please use a different email.")
        elif CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different username.")
        else:
            # Create the user if both email and username don't exist
            user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name,
                                                  first_name=first_name, user_type=3)
            user.save()
            messages.success(request, "Successfully added student.")
            return HttpResponseRedirect(reverse("show_login"))
        
    else:
        pass 
    return render(request, "signup_student_page.html")
