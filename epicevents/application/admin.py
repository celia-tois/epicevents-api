from django.contrib import admin
from application.models import User, Client, Contract, Event


class AdminPermissions(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(User)
admin.site.register(Client, AdminPermissions)
admin.site.register(Contract, AdminPermissions)
admin.site.register(Event, AdminPermissions)
