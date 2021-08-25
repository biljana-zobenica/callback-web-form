from django.contrib import admin
from django.db.models import query
from .models import Callback

# Register your models here.

@admin.action(description='Mark selected forms as archieved')
def make_archieved(modeladmin, request, queryset):
    queryset.update(status='a')

class CallbackAdmin (admin.ModelAdmin):
    list_display = ('subject', 'name', 'comment', 'status', 'submitted_date_time', 'support_date_time')
    list_filter = ('submitted_date_time', 'support_date_time')
    actions = [make_archieved]

    #def has_delete_permission(self, request, obj=None):
    #    return False

admin.site.register(Callback, CallbackAdmin)


# we woudl apply this if we want the superuser to have permission to delete users' forms
    #def has_delete_permission(request, obj=None):
    #    return request.user.is_superuser()