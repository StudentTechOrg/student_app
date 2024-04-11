
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from student_app import views, StudentViews
from student_system import settings

urlpatterns = [
    path('demo',views.showDemoPage),
    path('signup_student',views.signup_student,name="signup_student"),
    path('do_admin_signup',views.do_admin_signup,name="do_admin_signup"),
    path('do_signup_student',views.do_signup_student,name="do_signup_student"),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.ShowLoginPage,name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
    path('doLogin',views.doLogin,name="do_login"),
   

    

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
    path('testurl/',views.Testurl)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
