from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import LoginView, SignUpView

# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register('user', LoginViewSet)
urlpatterns = [
    path('v1/signup', SignUpView.as_view()),
    path('v1/login', LoginView.as_view()),
]
