from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from books.serializers import BookSerializer
from books import models as books_models


class BookViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    queryset = books_models.Book.objects.all()
