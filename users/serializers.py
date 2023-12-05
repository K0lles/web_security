from rest_framework.serializers import ModelSerializer

from users import models as user_models
from users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = user_models.User
        fields = "__all__"

    def create(self, validated_data: dict) -> User:
        password = validated_data.pop("password", None)
        user = User(
            **{field: value for field, value in validated_data.items()}
        )
        user.set_password(password)
        user.save()
        return user
