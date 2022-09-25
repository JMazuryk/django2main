from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from apps.cars.models import CarModel
from apps.cars.serializers import CarAllSerializer, CarSerializer


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarAllSerializer

    def get_queryset(self):
        # year_gt = self.request.query_params.get('year_gt')
        # if year_gt:
        #     return self.queryset.filter(year__gt=year_gt)
        queryset = super().get_queryset()
        # queryset = queryset.order_by('brand', 'year')
        # queryset = queryset.exclude(brand='acura ').order_by('brand', 'year')
        # queryset = queryset[:3]
        # queryset = queryset[2:4]
        # queryset = queryset.order_by('id').reverse()
        print(queryset.count())
        return queryset


# class CarListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get_serializer(self, *args, **kwargs):
#         if self.request.method == 'GET':
#             return CarAllSerializer(*args, **kwargs)
#         return super().get_serializer(*args, **kwargs)
#
#     def get_queryset(self):
#         year_gt = self.request.query_params.get('year_gt')
#         if year_gt:
#             return self.queryset.filter(year__gt=year_gt)
#             return super().get_queryset()

#
# def get(self, *args, **kwargs):
#     return super().list(*args, **kwargs)
#     # # year_gt = self.request.query_params.get('year_gt')
#     # # qs = CarModel.objects.all()
#     # # if year_gt:
#     # #     qs = qs.filter(year__gt=year_gt)
#     # #     # qs = qs.filter(year__gt=year_gt)
#     # #     #   qs = qs.filter(Q(band='volvo'), (Q(year=2015)|Q(price=10000)))
#     # serializer = self.get_serializer(self.get_queryset(), many=True)
#     # return Response(serializer.data, status.HTTP_200_OK)
#
#
#     #
#
#
# def post(self, *args, **kwargs):
#     return super().create(*args, **kwargs)
#
#
# # data = self.request.data
# # serializer = self.get_serializer(data=data)
# # serializer.is_valid(raise_exception=True)
# # serializer.save()
# # return Response(serializer.data, status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    # def get(self, *args, **kwargs):
    #     return super().retrieve(*args, **kwargs)
    #
    #     # # pk = kwargs.get('pk')
    #     # # car = get_object_or_404(CarModel, pk=pk)
    #     # car = self.get_object()
    #     # serializer = self.get_serializer(car)
    #     # return Response(serializer.data, status.HTTP_200_OK)
    #
    # def put(self, *args, **kwargs):
    #     return super().update(*args, **kwargs)
    #
    #     # pk = kwargs.get('pk')
    #     # car = get_object_or_404(CarModel, pk=pk)
    #     # car = self.get_object()
    #     # data = self.request.data
    #     # serializer = self.get_serializer(car, data)
    #     # serializer.is_valid(raise_exception=True)
    #     # serializer.save()
    #     # return Response(serializer.data, status.HTTP_200_OK)
    #
    # def patch(self, *args, **kwargs):
    #     return super().partial_update(*args, **kwargs)
    #
    #     # pk = kwargs.get('pk')
    #     # car = get_object_or_404(CarModel, pk=pk)
    #     # car = self.get_object()
    #     # data = self.request.data
    #     # serializer = self.get_serializer(car, data, partial=True)
    #     # serializer.is_valid(raise_exception=True)
    #     # serializer.save()
    #     # return Response(serializer.data, status.HTTP_200_OK)
    #
    # def delete(self, *args, **kwargs):
    #     return super().destroy(*args, **kwargs)
    #     # pk = kwargs.get('pk')
    #     # car = get_object_or_404(CarModel, pk=pk)
    #     car = self.get_object()
    #     # car.delete()
    #     # return Response(status=status.HTTP_204_NO_CONTENT)

# class CarRetrieveUpdateDestroy(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         return super().retrieve(*args, **kwargs)
#
#         # # pk = kwargs.get('pk')
#         # # car = get_object_or_404(CarModel, pk=pk)
#         # car = self.get_object()
#         # serializer = self.get_serializer(car)
#         # return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         return super().update(*args, **kwargs)
#
#         # pk = kwargs.get('pk')
#         # car = get_object_or_404(CarModel, pk=pk)
#         # car = self.get_object()
#         # data = self.request.data
#         # serializer = self.get_serializer(car, data)
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         # return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         return super().partial_update(*args, **kwargs)
#
#         # pk = kwargs.get('pk')
#         # car = get_object_or_404(CarModel, pk=pk)
#         # car = self.get_object()
#         # data = self.request.data
#         # serializer = self.get_serializer(car, data, partial=True)
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         # return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         return super().destroy(*args, **kwargs)
#         # pk = kwargs.get('pk')
#         # car = get_object_or_404(CarModel, pk=pk)
#         car = self.get_object()
#         # car.delete()
#         # return Response(status=status.HTTP_204_NO_CONTENT)
