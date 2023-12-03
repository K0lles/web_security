from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from books.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
