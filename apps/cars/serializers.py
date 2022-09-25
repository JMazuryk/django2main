from django.core.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.cars.models import CarModel


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year')

    # def validate_year(self, year: int):
    #     if str(year)[-2] == '2':
    #         raise ValidationError('pararam')
    #     return year
    #
    # def validate(self, attrs):
    #     year = attrs.get('year')
    #     price = attrs.get('price')
    #     if year == price:
    #         raise ValidationError('year == price')
    #     return super().validate(attrs)
    #


class CarAllSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'price')
