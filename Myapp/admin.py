from django.contrib import admin
from .models import Blood,Cylinder,Doctor,Hospital,Availability,Organ

admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Blood)
admin.site.register(Cylinder)
admin.site.register(Availability)
admin.site.register(Organ)