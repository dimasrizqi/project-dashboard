from django.contrib import admin
from .models import Assetmaster, License, Device

# Register your models here.
admin.site.register(Assetmaster)
admin.site.register(Device)
admin.site.register(License)