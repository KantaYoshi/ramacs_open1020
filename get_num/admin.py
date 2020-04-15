from django.contrib import admin

# Register your models here.
from .models import Log

@admin.register(Log)
class LogAdimin(admin.ModelAdmin):
    pass
