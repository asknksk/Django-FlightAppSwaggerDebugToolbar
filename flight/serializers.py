from dataclasses import fields
from rest_framework import serializers
from .models import Flight, Passanger, Reservation

class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = ( 
            "flight_number",
            "operating_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd",
        ) 
        