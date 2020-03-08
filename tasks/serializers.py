from rest_framework import serializers

from django.contrib.auth.models import User, Group
from .models import Task



class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'email',]




class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'tsk_title', 'tsk_status', 'tsk_assignted_time']








