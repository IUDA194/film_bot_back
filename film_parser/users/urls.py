from django.urls import path

from users.views import UserGetOrCreateView, UserStatisticsView

urlpatterns = [
    path('user/', UserGetOrCreateView.as_view()),
    path('user-statistics/', UserStatisticsView.as_view(), name='user-statistics'),
]
