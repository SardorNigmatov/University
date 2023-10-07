from django.contrib import admin
from .models import Faculty, Kafedra

# Register your models here.

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Kafedra)
class KafedraAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
