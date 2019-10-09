from django.contrib import admin

# Register your models here.
from .models import dustbin,Area,street

admin.site.register(dustbin)
admin.site.register(Area)
admin.site.register(street)


