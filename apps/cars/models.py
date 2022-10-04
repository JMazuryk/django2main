from django.db import models
from django.core import validators as v
from datetime import date

from apps.auto_parks.models import AutoParkModel
from apps.cars.managers import CarManager


# Create your models here.

# Створити модель Car з такими полями:
# - марка машини
# - рік випуску
# - кількість місць
# - тип кузову
# - об'єм двигуна (float)
#
# реалізувати всі CRUD операції
#
# ***при виведені всіх машин показувати тільки (id, марку машини та рік)

class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20, validators=(v.MinLengthValidator(3),), blank=True)
    year = models.IntegerField(validators=(v.MinValueValidator(1990), v.MaxValueValidator(date.today().year)), null=True)
    price = models.IntegerField(validators=(v.MinValueValidator(0), v.MaxValueValidator(10000000)), default=50000)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CarManager()
