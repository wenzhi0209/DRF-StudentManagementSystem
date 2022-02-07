from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User,UserProfile
# Register your models here.

class UserAdmin(UserAdmin):
    list_display=('email','is_staff','is_student','is_admin')
    list_filter=('is_admin',)
    fieldsets=(
        ('User Info',{
            'fields':('email','password')
        }),
        ('Permissions',{
            'fields':('is_staff','is_student','is_admin')
        }),
    )

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2'),
        }
        ),
    )

    search_fields=('email',)
    ordering=('email',)
    filter_horizontal=()

class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(User,UserAdmin)
admin.site.register(UserProfile,UserProfileAdmin)