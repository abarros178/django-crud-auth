from django.contrib import admin
from .models import Task

class Taskadmin(admin.ModelAdmin):
    readonly_fields = ("creadodate",)


admin.site.register(Task,Taskadmin)

# Register your models here.
