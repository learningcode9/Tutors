from django.contrib import admin
from .models import Category,tutors,Comment,ratings

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


class CommentAdmin(admin.ModelAdmin):
    list_display=('name','post','body','created','updated','active') 
    list_filter=('active','created','updated')  
    search_fields=('name','body')  
admin.site.register(Comment,CommentAdmin) 

class ratingAdmin(admin.ModelAdmin):
    list_display=['username','rating','tutorname']

admin.site.register(ratings,ratingAdmin)

