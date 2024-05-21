from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from . models import Project, Todo
from .serializers import ProjectSerializer, TodoSerializer, TodoCommentSerializer

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes  = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def comment(self, request, pk=None):
        todo = self.get_object()
        serializer = TodoCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(todo=todo,author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)