from django import forms
from django.forms import ChoiceField

from student_app.models import Courses,Students,Module

class ChoiceNoValidation(ChoiceField):
    def validate(self, value):
        pass

class DateInput(forms.DateInput):
    input_type = "date"

class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control", "autocomplete": "off"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", max_length=50, widget=forms.FileInput(attrs={"class": "form-control"}))
    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    sex = forms.ChoiceField(label="Sex", choices=gender_choice, widget=forms.Select(attrs={"class": "form-control"}))
    

    COUNTRY_CHOICES = [
        ("", "Select Country"),
        ("USA", "USA"),
        ("UK", "UK"),
        ("CAN", "Canada"),
        ("AUS", "Australia"),
    ]
    country = forms.ChoiceField(label="Country", choices=COUNTRY_CHOICES, widget=forms.Select(attrs={"class": "form-control"}))

    city = forms.CharField(label="City", max_length=50, widget=forms.Select(attrs={"class": "form-control"}))
 


class EditStudentForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


    gender_choice=(
        ("Male","Male"),
        ("Female","Female")
    )

    sex=forms.ChoiceField(label="Sex",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
    COUNTRY_CHOICES = [
        ("", "Select Country"),
        ("USA", "USA"),
        ("UK", "UK"),
        ("CAN", "Canada"),
        ("AUS", "Australia"),
    ]
    country = forms.ChoiceField(label="Country", choices=COUNTRY_CHOICES, widget=forms.Select(attrs={"class": "form-control"}))
    city = forms.CharField(label="City", max_length=50, widget=forms.Select(attrs={"class": "form-control"}))
 

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

class CourseForm(forms.Form):
    course_name=forms.CharField(label="Course Name",max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))

class ModuleForm(forms.Form):
    courses = Courses.objects.all()
    course_choices = [(course.id, course.course_name) for course in courses]

    availability_choices = [
        (True, "Open"),
        (False, "Close"),
    ]

    course = forms.ChoiceField(label="Course", choices=course_choices, widget=forms.Select(attrs={"class":"form-control"}))
    name = forms.CharField(label="Module Name", max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    code = forms.CharField(label="Code", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    credit = forms.IntegerField(label="Credit", widget=forms.NumberInput(attrs={"class": "form-control"}))
    category = forms.CharField(label="Category", max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={"class": "form-control"}))
    availability = forms.ChoiceField(label="Availability", choices=availability_choices, widget=forms.Select(attrs={"class": "form-control"}))


        
