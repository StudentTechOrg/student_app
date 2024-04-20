import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm
from datetime import datetime




from student_app.models import Students, Courses, CustomUser, \
     FeedBackStudent, NotificationStudent,ContactMessage,Module


def student_home(request):
    student=Students.objects.get(admin=request.user.id)

    return render(request,"student_template/student_home_template.html",{"student":student})



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
    user = CustomUser.objects.get(id=request.user.id)
    student = Students.objects.get(admin=user)
    
    COUNTRY_CITIES = {
        "USA": ["New York", "Los Angeles", "Chicago", "Houston", "San Francisco"],
        "UK": ["London", "Manchester", "Birmingham", "Glasgow", "Liverpool"],
        "CAN": ["Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa"],
        "AUS": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"],
    }

    context = {
        "user": user,
        "student": student,
        "COUNTRY_CITIES": COUNTRY_CITIES,
    }

    return render(request, "student_template/student_profile.html", context)


def student_profile_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("student_profile"))
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        address = request.POST.get("address")
        date_of_birth_str = request.POST.get("date_of_birth") 
        country = request.POST.get("country")
        city = request.POST.get("city")
        profile_picture = request.FILES.get('profile_picture')

        if not first_name or not last_name or not address or not date_of_birth_str or not country or not city:
            messages.error(request, "Please fill in all required fields.")
            return HttpResponseRedirect(reverse("student_profile"))

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password:
                customuser.set_password(password)
            customuser.save()

            student, created = Students.objects.get_or_create(admin=customuser)
            student.address = address
            student.country = country
            student.city = city
            if profile_picture:
                student.profile_pic = profile_picture
            
            date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d")
            student.date_of_birth = date_of_birth

            student.save()
            messages.success(request, "Successfully Updated Profile")
        except CustomUser.DoesNotExist:
            messages.error(request, "User does not exist.")
        except Exception as e:
            messages.error(request, f"Failed to update profile: {str(e)}")

        return HttpResponseRedirect(reverse("student_profile"))

        
def contact_us_submit(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("contact_us"))
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            student = CustomUser.objects.get(id=request.user.id)
      
            contact_entry = ContactMessage.objects.create(name=name, email=email, subject=subject, message=message,  student_id= student.id)
            contact_entry.save()

            messages.success(request, "Your message has been sent successfully!")
            return HttpResponseRedirect(reverse("contact_us"))  
        else:
            messages.error(request, "Failed to send message. Please check your input.")
            return HttpResponseRedirect(reverse("contact_us"))  



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
    student=Students.objects.get(admin=request.user.id)
    return render(request, 'about/about_us.html',{"student":student})


def who_we_are(request):
    student=Students.objects.get(admin=request.user.id)
    return render (request,'about/who_we_are.html',{"student":student})


def our_values(request):
    student=Students.objects.get(admin=request.user.id)
    return render (request,'about/our_values.html',{"student":student})


def strategy(request):
    student=Students.objects.get(admin=request.user.id)
    return render (request,'about/strategy.html',{"student":student})

def contact_us(request):
    student=Students.objects.get(admin=request.user.id)
    return render (request,'contact/contact_us.html',{"student":student})

def course_template(request):
    student=Students.objects.get(admin=request.user.id)
    course = Courses.objects.all()
    modules = Module.objects.all()
    return render(request, 'student_template/course_template.html', {'course': course, 'modules': modules,"student":student})


def module_detail(request, module_id):
    try:
        module = Module.objects.get(pk=module_id)
    except Module.DoesNotExist:
        raise Http404("Module does not exist")
    return render(request, 'student_template/module_detail.html', {'module': module})