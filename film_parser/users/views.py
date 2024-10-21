from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer, UserStatisticsSerializer

from django.utils import timezone
from datetime import timedelta

class UserGetOrCreateView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"error": "user_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        # get_or_create user by user_id
        user, created = User.objects.get_or_create(
            user_id=str(user_id)
        )

        # Update last_active field to the current time
        user.last_active = timezone.now()
        user.save(update_fields=['last_active'])

        # Serialize user data
        serializer = self.get_serializer(user)

        # Return serialized data with status indicating whether user was created or not
        return Response({
            "user": serializer.data,
            "created": created
        }, status=status.HTTP_200_OK)
        
class UserStatisticsView(generics.GenericAPIView):
    serializer_class = UserStatisticsSerializer

    def get(self, request, *args, **kwargs):
        # Общее количество пользователей
        total_users = User.objects.count()

        # Даты для периодов: день, неделя и месяц
        today = timezone.now().date()
        week_ago = today - timedelta(days=7)
        month_ago = today - timedelta(days=30)

        # Новые пользователи за день, неделю и месяц
        new_users_today = User.objects.filter(created_at__date=today).count()
        new_users_week = User.objects.filter(created_at__date__gte=week_ago).count()
        new_users_month = User.objects.filter(created_at__date__gte=month_ago).count()

        # Активные пользователи за день, неделю и месяц
        active_users_today = User.objects.filter(last_active__date=today).count()
        active_users_week = User.objects.filter(last_active__date__gte=week_ago).count()
        active_users_month = User.objects.filter(last_active__date__gte=month_ago).count()

        # Подготовка данных для сериализатора
        data = {
            "total_users": total_users,
            "new_users_today": new_users_today,
            "new_users_week": new_users_week,
            "new_users_month": new_users_month,
            "active_users_today": active_users_today,
            "active_users_week": active_users_week,
            "active_users_month": active_users_month,
        }

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)