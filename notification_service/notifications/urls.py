from django.urls import path
from .views import SendNotificationView, HealthCheckView

urlpatterns = [
    path(
        'api/notifications/send/',
        SendNotificationView.as_view(),
        name='send-notification',
    ),
    path('api/health/', HealthCheckView.as_view(), name='health-check'),
]
