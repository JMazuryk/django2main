from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, AllowAny

from .filters import CarFilter
from .models import CarModel
from .serializers import CarAllSerializer, CarSerializer
from core.pagination.page_pagimator import PagePagination


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarAllSerializer
    permission_classes = (IsAdminUser,)
    pagination_class = PagePagination
    filterset_class = CarFilter


class CarRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)


class CarCreateAPIView(CreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarAllSerializer
    permission_classes = (AllowAny,)
