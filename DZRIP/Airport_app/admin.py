from django.contrib import admin

# Register your models here.
from .models import Flight, Plane


admin.site.register(Flight)

admin.site.register(Plane)