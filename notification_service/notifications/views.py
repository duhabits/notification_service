from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NotificationSerializer
from .services import send_notification_email
import logging

logger = logging.getLogger(__name__)


class SendNotificationView(APIView):
    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"detail": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            send_notification_email(
                serializer.validated_data['recipient_email'],
                serializer.validated_data['notification_type'],
                serializer.validated_data['data'],
            )
            return Response(
                {
                    "status": "success",
                    "message": "Уведомление успешно отправлено",
                }
            )
        except Exception as e:
            logger.error(f"Ошибка сервера: {str(e)}")
            return Response(
                {"detail": "Ошибка при отправке уведомления"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class HealthCheckView(APIView):
    def get(self, request):
        return Response({"status": "ok"})
