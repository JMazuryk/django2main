from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


class TestView(APIView):
    def get(self, request):
        return Response("method get")

    def post(self, request):
        return Response("method post")

    def put(self, request):
        return Response("method put")

    def patch(self, request):
        return Response("method get")

    def delete(self, request):
        return Response("method delete")


users = [
    {'id': 1, 'name': 'Max', 'age': 18},
    {'id': 2, 'name': 'Vita', 'age': 20},
    {'id': 3, 'name': 'Orest', 'age': 35},
    {'id': 4, 'name': 'Taras', 'age': 40},
]


class UserListCreateView(APIView):
    def get(self, request):
        return Response(users)

    def post(self, *args, **kwargs):
        params_dict = self.request.query_params.dict()
        print(params_dict)
        new_user = self.request.data
        users.append(new_user)
        return Response(new_user)


class UserRetrieveUpdateDestroy(APIView):
    def get(self, *args, **kwargs):
        # print(kwargs.get('pk'))
        pk = kwargs.get('pk')
        for user in users:
            if user['id'] == pk:
                return Response(user)
            return Response('not found')
