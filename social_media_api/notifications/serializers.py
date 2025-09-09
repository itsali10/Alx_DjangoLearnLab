
from .models import Notification
from social_media_api.posts import serializers


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'timestamp']