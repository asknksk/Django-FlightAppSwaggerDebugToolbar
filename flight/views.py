from django.shortcuts import render

from flight.serializers import FlightSerializer
from .models import Flight, Passanger, Reservation
from rest_framework import viewsets
from .permissions import IsStafforReadOnly
# Create your views here.

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStafforReadOnly,)