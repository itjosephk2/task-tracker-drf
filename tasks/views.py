from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer


class RegisterView(APIView):
    """
    Register a new user.
    """
    permission_classes = []

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'User created successfully'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Task objects via the API.

    Provides list, retrieve, create, update, and delete actions
    using Django REST Framework's ModelViewSet.

    - Only authenticated users can access this view.
    - Users can only see and manage their own tasks.
    - When a task is created, it is automatically assigned
      to the currently logged-in user.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the new task with the currently authenticated user as the owner.
        """
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Return only the tasks that belong to the currently authenticated user.
        """
        return self.queryset.filter(owner=self.request.user)
