from rest_framework.generics import ListCreateAPIView

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer
