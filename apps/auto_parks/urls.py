from django.urls import path

from apps.auto_parks.views import AutoParkListCreateView, AutoParkAddCarView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view())
]
