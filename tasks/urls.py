from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TaskViewSet, RegisterView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]
