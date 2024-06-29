from django.contrib import admin
from .models import Member

class MembersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('department',)
    ordering = ('last_name',)
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'password')
        }),
        ('Personal info', {
            'fields': ()
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'department', 'user_permissions'),
        }),
    )

admin.site.register(Member, MembersAdmin)

# Register your models here.
