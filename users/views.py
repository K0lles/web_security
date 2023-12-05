from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from . import models as user_models
from . import serializers


class UserViewSet(ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = user_models.User.objects.all()
    permission_classes = [AllowAny]
