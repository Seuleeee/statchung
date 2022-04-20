from argparse import Namespace
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stats.views import AccountsViewSet, BoardsView, BoardsDetailView, DashboardRecentView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'accounts', AccountsViewSet, basename='accounts')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('v1/', include((router.urls, 'accounts'))),
    path('v1/boards/', BoardsView.as_view(), name='boards'),
    path('v1/boards/<int:pk>', BoardsDetailView.as_view(), name='boards_detail'),
    path('v1/dashboards/recent', DashboardRecentView.as_view(), name='dashboards_recent'),
]
