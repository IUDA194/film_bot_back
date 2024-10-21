import uuid

from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'ref_id', 'subscribed', 'subscription_start_date', 'free_daily_limit']

    def create(self, validated_data):
        if 'ref_id' not in validated_data or not validated_data['ref_id']:
            validated_data['ref_id'] = str(uuid.uuid4())
        return super().create(validated_data)

class UserStatisticsSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    new_users_today = serializers.IntegerField()
    new_users_week = serializers.IntegerField()
    new_users_month = serializers.IntegerField()
    active_users_today = serializers.IntegerField()
    active_users_week = serializers.IntegerField()
    active_users_month = serializers.IntegerField()
