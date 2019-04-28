from rest_framework import viewsets
from .models import Article
from .serializers import Article_serializer


class Article_viewset(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('posted_date')
    serializer_class = Article_serializer
