from djoser.views import UserViewSet

from users.models import User
from .serializers import UserSerializers


class UserViewSet(UserViewSet):
    """Вьюсет для пользователей и авторов."""
    quryset = User.objects.all()
    serializer_class = UserSerializers
