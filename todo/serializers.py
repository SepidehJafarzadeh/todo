from rest_framework import serializers
from .models import Project, Todo, TodoComment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TodoCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = TodoComment
        fields = "__all__"

class TodoSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)
    comments = TodoCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"