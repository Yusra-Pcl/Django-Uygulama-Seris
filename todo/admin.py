from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'completed', 'created_at')
    list_editable = ('completed', 'priority')
    list_filter = ('completed', 'priority')
