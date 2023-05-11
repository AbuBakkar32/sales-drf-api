from django.urls import path, include
from .views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    path('register/', RegistrationAPIView, name="user-register"),
    path('login/', LoginAPIView.as_view(), name='user-login'),
]
