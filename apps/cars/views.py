from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from .models import CarModel
from .serializers import CarAllSerializer, CarSerializer


class CarListView(ListAPIView):
    queryset = CarModel.objects.get_by_price_gt(5000)
    serializer_class = CarAllSerializer
    permission_classes = (IsAdminUser,)


class CarRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
