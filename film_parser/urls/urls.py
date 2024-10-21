from django.urls import path
from .views import UrlListView

urlpatterns = [
    path('list/', UrlListView.as_view(), name='url-list'),
]