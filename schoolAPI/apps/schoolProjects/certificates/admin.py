
from django.contrib import admin
from .models import Certificate
# Register your models here.

class CertificateAdmin(admin.ModelAdmin):
    list_display=('name','created_at','updated_at',)
    list_filter=('name','created_at','updated_at',)
    search_fields=('name',)


    

admin.site.register(Certificate,CertificateAdmin)