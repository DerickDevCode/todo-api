from rest_framework.routers import DefaultRouter

from todo.tasks.views import TaskViewSet, UserViewSet

router = DefaultRouter()
router.register(r'api/v1/tasks', TaskViewSet, basename='task')
router.register(r'api/v1/users', UserViewSet, basename='user')

urlpatterns = router.urls
