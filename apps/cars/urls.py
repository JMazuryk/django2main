from django.urls import path

from apps.cars.views import CarListView, CarRetrieveUpdateDestroy

urlpatterns = [
    path('', CarListView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroy.as_view())
]
