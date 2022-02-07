from django.contrib import admin
from .models import WaitlistEntry
# Register your models here.

class WaitlistEntryAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','created_at','updated_at',)
    list_filter=('first_name','last_name','created_at','updated_at',)
    search_fields=('first_name','last_name','email')


    

admin.site.register(WaitlistEntry,WaitlistEntryAdmin)
