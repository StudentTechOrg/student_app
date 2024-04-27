from rest_framework import serializers
from student_app.models import CustomUser,Students

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'user_type'] 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__' 
