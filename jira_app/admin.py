from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

from .models import CustomUser, EmployeeBankDetails, EmployeeDetails, DepartmentDetails, ClientDetails

# Register your models here.

#Add CustomUser Fields to Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Retain the default fields from UserAdmin and add custom fields
    list_display = UserAdmin.list_display + ('user_data',)  # Add 'user_data' to list view

    # Retain the default fieldsets from UserAdmin and add custom fields
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('user_data',)}),  # Add 'user_data' to the detail form
    )

    # Retain the default add_fieldsets from UserAdmin and add custom fields
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('user_data',),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(EmployeeBankDetails)
admin.site.register(EmployeeDetails)
admin.site.register(DepartmentDetails)
admin.site.register(ClientDetails)
