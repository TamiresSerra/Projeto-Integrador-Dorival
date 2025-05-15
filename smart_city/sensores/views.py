from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Sensor, Ambiente
from .serializers import SensorSerializer, AmbienteSerializer

class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    permission_classes = [IsAuthenticated]

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticated]
