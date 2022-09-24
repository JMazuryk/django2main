from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .serializers import UserSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import status

from .models import UserModel


# HW
# Створюємо в коні проекту файл users.json (в нього будете записувати ваших юзерів)
#
# Реалізовуємо ось такі EndPoints:
#
# GET http://localhost:8000/users           //витягнути всіх юзерів з файлу
# POST http://localhost:8000/users        // записати нового юзера в файл (не забудьте про id, він має бути унікальним)
#
# GET http://localhost:8000/users/<ID>           // витягти юзера по ID
# PUT http://localhost:8000/users/<ID>          // змінити юзера по ID
# DELETE  http://localhost:8000/users/<ID>          // видалити юзера по ID
#

# CW
#
# class TestView(APIView):
#     def get(self, request):
#         return Response("method get")
#
#     def post(self, request):
#         return Response("method post")
#
#     def put(self, request):
#         return Response("method put")
#
#     def patch(self, request):
#         return Response("method get")
#
#     def delete(self, request):
#         return Response("method delete")
#
#
# users = [
#     {'id': 1, 'name': 'Max', 'age': 18},
#     {'id': 2, 'name': 'Vita', 'age': 20},
#     {'id': 3, 'name': 'Orest', 'age': 35},
#     {'id': 4, 'name': 'Taras', 'age': 40},
# ]
#
#
# class UserListCreateView(APIView):
#     def get(self, request):
#         return Response(users)
#
#     def post(self, *args, **kwargs):
#         params_dict = self.request.query_params.dict()
#         print(params_dict)
#         new_user = self.request.data
#         users.append(new_user)
#         return Response(new_user)
#
#
# class UserRetrieveUpdateDestroy(APIView):
#     def get(self, *args, **kwargs):
#         # print(kwargs.get('pk'))
#         pk = kwargs.get('pk')
#         for user in users:
#             if user['id'] == pk:
#                 return Response(user)
#             return Response('not found')

class UserListCreateView(APIView):
    def get(self, *args, **kwargs):
        qs = UserModel.objects.all()
        # res = [model_to_dict(user) for user in qs]
        # print(qs)
        serializer = UserSerializer(qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        # data = self.request.data
        # user = UserModel(**data)
        # user.save()
        # return Response(model_to_dict(user))
        data = self.request.data
        serializer = UserSerializer(data=data)
        # if not serializer.is_valid():
        #     return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        # qs = UserModel.objects.filter(pk=pk)
        # exists = qs.exists()
        # if not exists:
        #     return Response('Not found user')
        # # user = qs.first()
        # user = UserModel.objects.get(pk=pk)
        # # return Response(model_to_dict(user))
        user = get_object_or_404(UserModel, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        # qs = UserModel.objects.filter(pk=pk)
        # exists = qs.exists()
        # if not exists:
        #     return Response('Not found user')
        # data = self.request.data
        # qs.update(**data)
        # user = UserModel.objects.get(pk=pk)
        # # name = data.get('name')
        # # age = data.get('age')
        # # user.name = name
        # # user.age = age
        # # user.save()
        # return Response(model_to_dict(user))
        user = get_object_or_404(UserModel, pk=pk)
        data = self.request.data
        serializer = UserSerializer(user, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        data = self.request.data
        serializer = UserSerializer(user, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        # qs = UserModel.objects.filter(pk=pk)
        # exists = qs.exists()
        # if not exists:
        #     return Response('Not found user')
        # user = UserModel.objects.get(pk=pk)
        # user.delete()
        user = get_object_or_404(UserModel, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
