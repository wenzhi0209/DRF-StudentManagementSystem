
from django.contrib import admin
from .models import Lecture
# Register your models here.

class LectureAdmin(admin.ModelAdmin):
    list_display=('title','date','lecturer_name',)
    list_filter=('title','date','lecturer_name',)
    search_fields=('title','lecturer_name')


    

admin.site.register(Lecture,LectureAdmin)