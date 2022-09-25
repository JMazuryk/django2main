from django.urls import path

from apps.cars.views import CarListCreateView, CarRetrieveUpdateDestroy

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroy.as_view())
]
