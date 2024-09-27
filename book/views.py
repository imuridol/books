from rest_framework import viewsets
from .serializers import AuthorModelSerializer
from .models import Author


class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer