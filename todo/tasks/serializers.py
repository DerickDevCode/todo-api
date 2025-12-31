from rest_framework import serializers

from todo.base.models import User
from todo.tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'titulo', 'descricao', 'status', 'user']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'date_joined': {'read_only': True}
        }
        model = User
        fields = ['id', 'name', 'email', 'date_joined', 'tasks']
