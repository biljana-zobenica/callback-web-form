from django.contrib import admin
from django.db.models import query
from .models import CallbackForm

# Register your models here.

@admin.action(description='Mark selected forms as archieved')
def make_archieved(modeladmin, request, queryset):
    queryset.update(status='a')

class CallbackFormAdmin (admin.ModelAdmin):
    list_display = ('subject', 'name', 'comment', 'status')
    list_filter = ('submitted_date_time', 'support_date_time')
    actions = [make_archieved]

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

admin.site.register(CallbackForm, CallbackFormAdmin)

