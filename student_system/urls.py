
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from student_app import views, StudentViews,AdminViews
from student_system import settings
from django.contrib import admin


urlpatterns = [
    path('demo',views.showDemoPage),
    path('signup_student',views.signup_student,name="signup_student"),
    path('signup_admin',views.signup_admin,name="signup_admin"),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.ShowLoginPage,name="show_login"),
    path('get_user_details', views.GetUserDetails),


    #rest api 
    path('api/student/signup/', views.student_signup, name='student-signup'),
    path('api/login/', views.login_check, name='login_check'),
    path('api/logout/', views.logout_view, name='logout'),
    path('api/contactus/', StudentViews.contact_us_submit, name='contact_us_submit'),

    

    path('student_home', StudentViews.student_home, name="student_home"),
    path('student_feedback', StudentViews.student_feedback, name="student_feedback"),
    path('student_feedback_save', StudentViews.student_feedback_save, name="student_feedback_save"),
    path('student_profile', StudentViews.student_profile, name="student_profile"),
    path('student_profile_save', StudentViews.student_profile_save, name="student_profile_save"),
    path('student_fcmtoken_save', StudentViews.student_fcmtoken_save, name="student_fcmtoken_save"),
    path('student_all_notification',StudentViews.student_all_notification,name="student_all_notification"),
    path('about_us',StudentViews.about_us,name="about_us"),
    path('about_us/who_we_are',StudentViews.who_we_are,name="who_we_are"),
    path('about_us/our_values',StudentViews.our_values,name="our_values"),
    path('about_us/strategy',StudentViews.strategy,name="strategy"),
    path('contact_us',StudentViews.contact_us,name="contact_us"),
    path('course_template',StudentViews.course_template,name="course_template"),
    path('module/<int:module_id>/', StudentViews.module_detail, name='module_detail'),
     path('register_module/<int:module_id>/', StudentViews.register_module, name='register_module'),
      path('unregister_module/<int:module_id>/', StudentViews.unregister_module, name='unregister_module'),

    # Admin
     path('admin_home',AdminViews.admin_home,name="admin_home"),
    path('add_student', AdminViews.add_student,name="add_student"),
    path('add_student_save', AdminViews.add_student_save,name="add_student_save"),
    path('manage_student', AdminViews.manage_student,name="manage_student"),
    path('edit_student/<str:student_id>', AdminViews.edit_student,name="edit_student"),
    path('edit_student_save', AdminViews.edit_student_save,name="edit_student_save"),
    path('check_email_exist', AdminViews.check_email_exist,name="check_email_exist"),
    path('check_username_exist', AdminViews.check_username_exist,name="check_username_exist"),
    path('student_feedback_message', AdminViews.student_feedback_message,name="student_feedback_message"),
    path('student_feedback_message_replied', AdminViews.student_feedback_message_replied,name="student_feedback_message_replied"),
    path('admin_profile', AdminViews.admin_profile,name="admin_profile"),
    path('admin_profile_save', AdminViews.admin_profile_save,name="admin_profile_save"),
    path('admin_send_notification_student', AdminViews.admin_send_notification_student,name="admin_send_notification_student"),
    path('send_student_notification', AdminViews.send_student_notification,name="send_student_notification"),
    path('student_enquiries', AdminViews.student_enquiries,name="student_enquiries"),
    path('add_course', AdminViews.add_course, name='add_course'),
    path('add_course_save', AdminViews.add_course_save,name="add_course_save"),
    path('add_module', AdminViews.add_module, name='add_module'),
    path('add_module_save', AdminViews.add_module_save,name="add_module_save"),
    path('module_list', AdminViews.module_list, name='module_list'),
    path("manage_course", AdminViews.manage_course, name='manage_course'),
    path("edit_course/<int:course_id>",AdminViews.edit_course, name='edit_course'),
    path("delete_course/<int:course_id>",AdminViews.delete_course, name='delete_course'),
    path("manage_module", AdminViews.manage_module, name='manage_module'),
    path("edit_module/<int:module_id>",AdminViews.edit_module, name='edit_module'),
    path("delete_module/<int:subject_id>",AdminViews.delete_module, name='delete_module'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
