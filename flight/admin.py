from django.contrib import admin
from .models import Flight, Passanger, Reservation

# Register your models here.
admin.site.register(Flight)
admin.site.register(Passanger)
admin.site.register(Reservation)