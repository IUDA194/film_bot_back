from rest_framework import generics
from urls.models import Url
from urls.serializers import UrlSerializer

class UrlListView(generics.ListAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
