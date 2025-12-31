from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.tasks.urls')),

    # Autenticação por Token DRF
    path('api-token-auth/', views.obtain_auth_token),

    # Autenticação por Session DRF
    path('api-auth/', include("rest_framework.urls")),

    # Autenticação por Token JWT com a biblioteca "djangorestframework-simplejwt"
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Endpoint que verifica a validade do Token JWT
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
