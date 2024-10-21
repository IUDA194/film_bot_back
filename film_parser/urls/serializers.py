from rest_framework import serializers
from urls.models import Url

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['id', 'channel_name', 'channel_chat_id', 'channel_url', 'created_at']
