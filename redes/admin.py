from django.contrib import admin
from .models import Redes
# Register your models here.
class RedesAdmin(admin.ModelAdmin):
    readonly_fields=('create', 'updated')
admin.site.register(Redes, RedesAdmin)