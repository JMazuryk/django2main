from django.urls import path

from apps.users.views import UserCreateView, AddAvatarView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/avatar', AddAvatarView.as_view())

]
