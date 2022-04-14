from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stats.views import StatsViewSet, UsersViewSet, DashboardViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'stats', StatsViewSet, basename='stats')
router.register(r'users', UsersViewSet, basename='users')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('v1/', include((router.urls, 'stats'))),
    path('v1/', include((router.urls, 'users'))),
    path('v1/dashboard/<str:stat>', DashboardViewSet.as_view())
]
