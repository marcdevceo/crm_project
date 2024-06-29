from django.contrib import admin
from .models import Record

class RecordsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zipcode')
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    list_filter = ('state', 'city')
    ordering = ('last_name',)
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name')
        }),
        ('Personal info', {
            'fields': ('email', 'phone', 'address', 'city', 'state')
        }),
        ('Permissions', {
            'fields': (),
        }),
    )

admin.site.register(Record, RecordsAdmin)
