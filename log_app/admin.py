from django.contrib import admin
from .models import Attende, Master

# Register your models here.
#admin.site.register(Attende)
@admin.register(Attende)
class AttendeAdmin(admin.ModelAdmin):
    #fields = ['room_name', 'uname', 'uid', 'purpose']
    list_filter = ['room_name', 'date']

#admin.site.register(Master)
@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ['uid', 'name', 'rfid_id']
    search_fields = ['uid', 'name', 'rfid_id']