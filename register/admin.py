from django.contrib import admin
from .models import Building
from .models import Address
# Register your models here.

admin.site.register(Building)
admin.site.register(Address)