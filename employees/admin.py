from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Admin panel configuration for Employee model"""
    
    list_display = ('emp_id', 'emp_name', 'emp_role', 'emp_loc', 'emp_ph_no', 'created_at')
    list_filter = ('emp_role', 'emp_loc', 'created_at')
    search_fields = ('emp_name', 'emp_ph_no', 'emp_role')
    readonly_fields = ('emp_id', 'created_at', 'updated_at')
    
    fieldsets = (
        ('Employee Information', {
            'fields': ('emp_id', 'emp_name', 'emp_role', 'emp_loc', 'emp_ph_no')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ('-created_at',)
