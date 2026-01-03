from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter

from todo.base.models import User
from todo.tasks.models import Task
from todo.tasks.serializers import TaskSerializer, UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Filtros e ordenação
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['status', 'criada_em']
    ordering_fields = ['status', 'criada_em']
    ordering = ['-criada_em']

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    # Filtros e ordenação
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'email', 'is_staff', 'is_active', 'date_joined']
    ordering_fields = ['name', 'email', 'is_staff', 'is_active', 'date_joined']
    ordering = ['-date_joined']
