from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(MyUser)
admin.site.register(Bloger)
admin.site.register(Business)
admin.site.register(City)
admin.site.register(Country)