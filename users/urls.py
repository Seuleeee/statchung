from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register('user', LoginViewSet)
urlpatterns = [
    path('v1/signup', views.signup),
    path('v1/login', views.login),
]
