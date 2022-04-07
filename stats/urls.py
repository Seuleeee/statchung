from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stats.views import StatsViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'stats', StatsViewSet, basename='stats')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('v1/', include((router.urls, 'stats'))),
]
