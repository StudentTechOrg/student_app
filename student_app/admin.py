from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from student_app.models import CustomUser


class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)