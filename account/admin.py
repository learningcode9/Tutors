from django.contrib import admin
from onlinetutors.models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','degree','created_at','updated_at']
    search_fields=('name','genres')
   
admin.site.register(Application,ApplicationAdmin)


