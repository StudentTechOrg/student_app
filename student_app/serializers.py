from rest_framework import serializers
from student_app.models import CustomUser,Students,ContactMessage

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'user_type'] 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__' 

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
