from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Employee)
admin.site.register(Drsadia)  # ✅ register it for admin
admin.site.register(DrHamid) 
admin.site.register(DrAhmed)  # ✅ register it for admin
admin.site.register(DrFaraz)
admin.site.register(DrImran)  # ✅ register it for admin
admin.site.register(DrNadia)
admin.site.register(DrSalman)  # ✅ register it for admin
admin.site.register(DrSara)
admin.site.register(LabAppointment)