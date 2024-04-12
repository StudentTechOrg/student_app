import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

from student_app.models import Students, Courses, Subjects, CustomUser, \
     FeedBackStudent, NotificationStudent, SessionYearModel


def student_home(request):
    student=Students.objects.get(admin=request.user.id)
    course=Courses.objects.get(id=student.course_id.id)
    subjects=Subjects.objects.filter(course_id=course).count()
  

    subject_name=[]
    subject_data=Subjects.objects.filter(course_id=student.course_id)
    for subject in subject_data:
        subject_name.append(subject.subject_name)

    return render(request,"student_template/student_home_template.html",{"subjects":subjects,"data_name":subject_name,"student":student})



def student_feedback(request):
    staff_id=Students.objects.get(admin=request.user.id)
    feedback_data=FeedBackStudent.objects.filter(student_id=staff_id)
    student=Students.objects.get(admin=request.user.id)
    return render(request,"student_template/student_feedback.html",{"feedback_data":feedback_data,"student":student})

def student_feedback_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("student_feedback"))
    else:
        feedback_msg=request.POST.get("feedback_msg")

        student_obj=Students.objects.get(admin=request.user.id)
        try:
            feedback=FeedBackStudent(student_id=student_obj,feedback=feedback_msg,feedback_reply="")
            feedback.save()
            messages.success(request, "Successfully Sent Feedback")
            return HttpResponseRedirect(reverse("student_feedback"))
        except:
            messages.error(request, "Failed To Send Feedback")
            return HttpResponseRedirect(reverse("student_feedback"))

def student_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    student=Students.objects.get(admin=user)
    return render(request,"student_template/student_profile.html",{"user":user,"student":student})

def student_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("student_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        address=request.POST.get("address")
        profile_picture = request.FILES['profile_picture']
       
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()

            student=Students.objects.get(admin=customuser)
            student.address=address
            student.profile_pic = profile_picture
            student.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("student_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("student_profile"))

@csrf_exempt
def student_fcmtoken_save(request):
    token=request.POST.get("token")
    try:
        student=Students.objects.get(admin=request.user.id)
        student.fcm_token=token
        student.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

def student_all_notification(request):
    student=Students.objects.get(admin=request.user.id)
    notifications=NotificationStudent.objects.filter(student_id=student.id)
    return render(request,"student_template/all_notification.html",{"notifications":notifications,"student":student})

 

   
def about_us(request):
    return render(request, 'about/about_us.html')


def who_we_are(request):
    return render (request,'about/who_we_are.html')


def our_values(request):
    return render (request,'about/our_values.html')


def strategy(request):
    return render (request,'about/strategy.html')

def contact_us(request):
    return render (request,'contact/contact_us.html')


