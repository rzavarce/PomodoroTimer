from rest_framework import serializers

from django.contrib.auth.models import User, Group
from .models import Task
from configs.models import Config


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'email',]



class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = ['cnf_lap_time', 'cnf_time_short_brake', 'cnf_time_long_brake']




class TaskSerializer(serializers.ModelSerializer):

	tsk_config = ConfigSerializer(read_only=True)

	class Meta:
		model = Task
		fields = ['id', 'tsk_title', 'tsk_status', 'tsk_assignted_time', 'tsk_config']




