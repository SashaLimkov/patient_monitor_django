from django.contrib import admin
from .models.markers import *
# Register your models here.
admin.site.register(Marker)
admin.site.register(Measurement)
admin.site.register(Condition)
admin.site.register(Deviations)
admin.site.register(MarkerCondition)
admin.site.register(UserState)
admin.site.register(PatientSystem)