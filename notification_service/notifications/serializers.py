from rest_framework import serializers


class NotificationSerializer(serializers.Serializer):
    recipient_email = serializers.EmailField()
    notification_type = serializers.ChoiceField(
        choices=['listing_viewed', 'contact_taken']
    )
    data = serializers.DictField()

    def validate_data(self, value):
        notification_type = self.initial_data.get('notification_type')

        if notification_type == 'listing_viewed' and 'view_count' not in value:
            raise serializers.ValidationError(
                "Для listing_viewed требуется view_count"
            )

        if (
            notification_type == 'contact_taken'
            and 'contact_count' not in value
        ):
            raise serializers.ValidationError(
                "Для contact_taken требуется contact_count"
            )

        return value
