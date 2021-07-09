from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
# Register your models here.
from .models import *


admin.site.register(MyUser)
admin.site.register(Bloger)

admin.site.register(City)
admin.site.register(Country)


@admin.register(Business)
class BusinessAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')