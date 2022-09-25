from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from cars.models import CarModel
from cars.serializers import CarAllSerializer, CarSerializer


class CarListCreateView(APIView):

    def get(self, *args, **kwargs):
        qs = CarModel.objects.all()
        serializer = CarAllSerializer(qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroy(APIView):

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        car = get_object_or_404(CarModel, pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        car = get_object_or_404(CarModel, pk=pk)
        data = self.request.data
        serializer = CarSerializer(car, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        car = get_object_or_404(CarModel, pk=pk)
        data = self.request.data
        serializer = CarSerializer(car, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self,*args,**kwargs):
        pk = kwargs.get('pk')
        car = get_object_or_404(CarModel,pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)