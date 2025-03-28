from django.contrib import admin
from .models import Materials
# Register your models here.

class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'uploaded_by', 'created_at')
    search_fields = ('title', 'uploaded_by__username')
admin.site.register(Materials, MaterialsAdmin)