from django.contrib import admin
from .models import Hotel, AdditionalService, Room

# Register your models here.
admin.site.register(Hotel)
admin.site.register(AdditionalService)
admin.site.register(Room)
