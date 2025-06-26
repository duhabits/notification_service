from django.core.mail import send_mail
from django.conf import settings
import logging

from .templates import NOTIFICATION_TEMPLATES


logger = logging.getLogger(__name__)


def send_notification_email(recipient_email, notification_type, data):
    try:
        template = NOTIFICATION_TEMPLATES[notification_type]
        subject = template['subject']
        message = template['message'].format(**data)

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            fail_silently=False,
        )
        logger.info(f"Уведомление успешно отправлено на {recipient_email}")
        return True
    except Exception as e:
        logger.error(f"Ошибка при отправке уведомления: {str(e)}")
        raise
