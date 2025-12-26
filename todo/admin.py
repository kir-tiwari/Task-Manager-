from django.contrib import admin
from .models import TODO

@admin.register(TODO)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date')
