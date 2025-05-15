from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, AmbienteViewSet

router = DefaultRouter()
router.register(r'sensores', SensorViewSet)
router.register(r'ambientes', AmbienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
