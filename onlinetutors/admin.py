from django.contrib import admin
from .models import Category,tutors

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(Category, CategoryAdmin)

class TutorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','Tagline','price','created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields=('name','Tagline',)
    list_editable = ['price',]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(tutors, TutorAdmin)

# class ApplicationAdmin(admin.ModelAdmin):
#     list_display=['firstname','lastname','degree','created_at','updated_at']
#     search_fields=('name','genres')
   
# admin.site.register(Application,ApplicationAdmin)
