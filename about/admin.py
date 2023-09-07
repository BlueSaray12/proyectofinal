from django.contrib import admin
from.models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin): 
    readonly_fields=('create','updated')
    list_display=('author', 'title', 'updated')
    search_fields=('author__username',)
admin.site.register(Project, ProjectAdmin)
