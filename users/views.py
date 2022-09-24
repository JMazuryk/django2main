import json
from typing import TypedDict
from rest_framework.views import APIView
from rest_framework.response import Response

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

User = TypedDict('User', {'id': int, 'name': str, 'age': int})
FILE = 'users.json'


class FileTools:
    @property
    def users(self) -> list[User]:
        try:
            with open(FILE) as file:
                return json.load(file)
        except:
            return []

    @staticmethod
    def save(users: list[User]) -> None:
        with open(FILE, 'w') as file:
            json.dump(users, file)


class UserListCreateView(APIView, FileTools):
    def get(self, *args, **kwargs):
        return Response(self.users)

    def post(self, *args, **kwargs):
        users = self.users
        user = self.request.data
        user['id'] = users[-1]['id'] + 1 if users else 1
        users.append(user)
        try:
            self.save(users)
        except:
            return Response('Error')
        return Response(user)


class UserRetrieveUpdateDestroyView(APIView, FileTools):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = next((item for item in self.users if item['id'] == pk), None)
        if not user:
            return Response('Not found user')
        return Response(user)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        users = self.users
        user = next((item for item in users if item['id'] == pk), None)
        if not user:
            return Response('User not found')
        user |= self.request.data
        try:
            self.save(users)
        except:
            return Response('Error')
        return Response (user)

    def delete (self, *args, **kwargs):
        pk = kwargs.get('pk')
        users = self.users
        index = next((i for i, item in enumerate (users) if item['id'] == pk), None)
        if index is None:
            return Response('User not found')
        del users[index]
        try:
            self.save(users)
        except:
            return Response('Error')
        return Response('deleted')


