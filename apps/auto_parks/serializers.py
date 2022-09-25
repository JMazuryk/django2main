from rest_framework.serializers import ModelSerializer

from apps.auto_parks.models import AutoParkModel
from apps.cars.serializers import CarSerializer


class AutoParkSerializer(ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    class Meta:

        model = AutoParkModel
        fields = ('id', 'name', 'cars')
