from typing import Type
from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.users.permissions import IsSuperUser
from apps.users.serializers import UserSerializer, AddAvatarSerializer
from apps.users.models import UserModel as User

UserModel: Type[User] = get_user_model()


class UserCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return IsSuperUser(),
        return super().get_permissions()


class AddAvatarView(UpdateAPIView):
    serializer_class = AddAvatarSerializer
    http_method_names = ('patch',)

    def get_object(self):
        return self.request.user.profile
