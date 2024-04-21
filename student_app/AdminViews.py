import json
import requests
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from student_app.forms import AddStudentForm, EditStudentForm,CourseForm,ModuleForm
from student_app.models import CustomUser, Courses, Students, \
    FeedBackStudent, ContactMessage, \
    NotificationStudent,Module\
    


def admin_home(request):
    total_students = Students.objects.all().count()
    total_module = Module.objects.all().count()
    total_course = Courses.objects.all().count()

    context = {
        'page_title': "Admin Dashboard",
        'total_students': total_students,
        'total_course': total_course,
        'total_module': total_module,

    }
    return render(request,"Admin_template/home_content.html", context)


def add_student(request):
    form=AddStudentForm()
    return render(request,"Admin_template/add_student_template.html",{"form":form})

def add_student_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("add_student"))
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        sex = request.POST.get("sex")
        profile_pic = request.FILES.get('profile_pic')
        date_of_birth_str = request.POST.get("date_of_birth") 
        country = request.POST.get("country")
        city = request.POST.get("city")

        if not first_name or not last_name or not username or not email or not password or not address or not sex :
            messages.error(request, "Please fill in all required fields.")
            return HttpResponseRedirect(reverse("add_student"))

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=3)
            user.students.address = address
            user.students.gender = sex
            user.students.country = country
            user.students.city = city
            if profile_pic:
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
                user.students.profile_pic = profile_pic_url

            user.save()
            user.students.save()

            messages.success(request, "Successfully Added Student")
        except Exception as e:
            messages.error(request, f"Failed to Add Student: {str(e)}")

        return HttpResponseRedirect(reverse("add_student"))     



def manage_student(request):
    students=Students.objects.all()
    return render(request,"Admin_template/manage_student_template.html",{"students":students})



def edit_student(request,student_id):
    request.session['student_id']=student_id
    student=Students.objects.get(admin=student_id)
    form=EditStudentForm()
    form.fields['email'].initial=student.admin.email
    form.fields['first_name'].initial=student.admin.first_name
    form.fields['last_name'].initial=student.admin.last_name
    form.fields['username'].initial=student.admin.username
    form.fields['address'].initial=student.address
    form.fields['sex'].initial=student.gender
    return render(request,"Admin_template/edit_student_template.html",{"form":form,"id":student_id,"username":student.admin.username,"student" :student})

def edit_student_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        student_id=request.session.get("student_id")
        if student_id==None:
            return HttpResponseRedirect(reverse("manage_student"))

        form=EditStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            sex = form.cleaned_data["sex"]

            if request.FILES.get('profile_pic',False):
                profile_pic=request.FILES['profile_pic']
                fs=FileSystemStorage()
                filename=fs.save(profile_pic.name,profile_pic)
                profile_pic_url=fs.url(filename)
            else:
                profile_pic_url=None


            try:
                user=CustomUser.objects.get(id=student_id)
                user.first_name=first_name
                user.last_name=last_name
                user.username=username
                user.email=email
                user.save()

                student=Students.objects.get(admin=student_id)
                student.address=address
                student.gender=sex
                if profile_pic_url!=None:
                    student.profile_pic=profile_pic_url
                student.save()
                del request.session['student_id']
                messages.success(request,"Successfully Edited Student")
                return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id}))
            except:
                messages.error(request,"Failed to Edit Student")
                return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id}))
        else:
            form=EditStudentForm(request.POST)
            student=Students.objects.get(admin=student_id)
            return render(request,"Admin_template/edit_student_template.html",{"form":form,"id":student_id,"username":student.admin.username})

@csrf_exempt
def check_email_exist(request):
    email=request.POST.get("email")
    user_obj=CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def check_username_exist(request):
    username=request.POST.get("username")
    user_obj=CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def student_feedback_message(request):
    feedbacks=FeedBackStudent.objects.all()
    return render(request,"Admin_template/student_feedback_template.html",{"feedbacks":feedbacks})

@csrf_exempt
def student_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedBackStudent.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")


@csrf_exempt

def admin_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    return render(request,"Admin_template/admin_profile.html",{"user":user})

def admin_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("admin_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            # if password!=None and password!="":
            #     customuser.set_password(password)
            customuser.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("admin_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("admin_profile"))

def admin_send_notification_student(request):
    students=Students.objects.all()
    return render(request,"Admin_template/student_notification.html",{"students":students})

def student_enquiries(request):
    enquiries=ContactMessage.objects.all()
    return render(request,"Admin_template/student_enquiries_template.html",{"enquiries":enquiries})


@csrf_exempt
def send_student_notification(request):
    id=request.POST.get("id")
    message=request.POST.get("message")
    student=Students.objects.get(admin=id)
    token=student.fcm_token
    url="https://fcm.googleapis.com/fcm/send"
    body={
        "notification":{
            "title":"Student Management System",
            "body":message,
            "click_action": "https://studentmanagementsystem22.herokuapp.com/student_all_notification",
            "icon": "http://studentmanagementsystem22.herokuapp.com/static/dist/img/user2-160x160.jpg"
        },
        "to":token
    }
    headers={"Content-Type":"application/json","Authorization":"key=SERVER_KEY_HERE"}
    data=requests.post(url,data=json.dumps(body),headers=headers)
    notification=NotificationStudent(student_id=student,message=message)
    notification.save()
    print(data.text)
    return HttpResponse("True")

def add_course(request):
    form=CourseForm()
    return render(request,"Admin_template/add_course_template.html",{"form":form})

def add_course_save(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course_name = form.cleaned_data['course_name']
            new_course = Courses(course_name=course_name)
            new_course.save()
            messages.success(request, "Course added successfully!")
            return HttpResponseRedirect(reverse("add_course"))
        else:
            messages.error(request, "Failed to add course. Please check your input.")
    else:
        form = CourseForm()
    return render(request, 'Admin_template/add_course_template.html', {'form': form})


def manage_course(request):
    courses = Courses.objects.all()
    return render(request, 'Admin_template/manage_course.html', {'courses': courses})   
  


def edit_course(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course.course_name = form.cleaned_data['course_name']
            try:
                course.save()
                messages.success(request, "Successfully Updated")
            except:
                messages.error(request, "Could Not Update")
        else:
            messages.error(request, "Form is not valid")
    else:
        form = CourseForm(initial={'name': course.course_name})

    context = {
        'form': form,
        'course_id': course_id,
    }
    
    return render(request, 'admin_template/edit_course_template.html', context)



def delete_course(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    try:
        course.delete()
        messages.success(request, "Course deleted successfully!")
    except Exception:
        messages.error(
            request, "Sorry, some students are assigned to this course already. Kindly change the affected student course and try again")
    return redirect(reverse('manage_course'))

def add_module(request):
    form=ModuleForm()
    return render(request,"Admin_template/add_module_template.html",{"form":form})


def add_module_save(request):
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            selected_course_id = form.cleaned_data['course']
            selected_course = Courses.objects.get(id=selected_course_id)  # Fetch the Courses instance
            name = form.cleaned_data['name']
            code = form.cleaned_data['code']
            credit = form.cleaned_data['credit']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            availability = form.cleaned_data['availability']
            
            new_module = Module(course_id=selected_course.id, name=name, code=code, credit=credit, category=category, description=description, availability=availability)
            new_module.save()
            messages.success(request, "Module added successfully!")
            return HttpResponseRedirect(reverse("add_module"))
        else:
            messages.error(request, "Failed to add module. Please check your input.")
            return render(request, 'Admin_template/add_module_template.html', {'form': form}) 
    else:
        return render(request, 'Admin_template/add_module_template.html', {'form': ModuleForm()})



def manage_module(request):
    modules = Module.objects.all()
    context = {
        'modules': modules,
    }
    return render(request, "Admin_template/manage_module.html", context)

def delete_module(request, subject_id):
    module = get_object_or_404(Module, id=subject_id)
    module.delete()
    messages.success(request, "Module deleted successfully!")
    return redirect(reverse('manage_module'))

def edit_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            module.name = form.cleaned_data['name']
            module.code = form.cleaned_data['code']
            module.credit = form.cleaned_data['credit']
            module.category = form.cleaned_data['category']
            module.description = form.cleaned_data['description']
            module.availability = form.cleaned_data['availability']
            try:
                module.save()
                messages.success(request, "Successfully Updated")
            except:
                messages.error(request, "Could Not Update")
        else:
            messages.error(request, "Form is not valid")
    else:
        form = ModuleForm(initial={
            'course': module.course.id,
            'name': module.name,
            'code': module.code,
            'credit': module.credit,
            'category': module.category,
            'description': module.description,
            'availability': module.availability,
        })

    context = {
        'form': form,
        'module_id': module_id,
    }
    
    return render(request, 'admin_template/edit_module_template.html', context)

    


def module_list(request):
    modules = Module.objects.all()
    return render(request, 'Admin_template/module_list.html', {'modules': modules})