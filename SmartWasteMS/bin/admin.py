from django.contrib import admin

# Register your models here.
from .models import dustbin,Area,street,stat_count

admin.site.register(dustbin)
admin.site.register(Area)
admin.site.register(street)
admin.site.register(stat_count)



