from django.contrib import admin
from .models import App


class AppAdmin(admin.ModelAdmin):
    list_display = ('title', 'app_id', 'description', 'url')
    list_filter = ('title', 'url')
    search_fields = ('title', 'url')
    ordering = ['app_id']


admin.site.register(App, AppAdmin)
