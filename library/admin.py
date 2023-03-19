from django.contrib import admin
from .models import *



# class AuthorAdmin(admin.ModelAdmin):
#     list_display=('first_name','last_name','genre')  
admin.site.register(Author)
# class BookInstanceAdmin(admin.TabularInline):
#     list_filter = ('status', 'due_back')

# class BooksInstanceInline(admin.TabularInline):
#     model = BookInstance    
# class BookAdmin(admin.ModelAdmin):
#     list_display=('title','author','genre')  
#     inlines = [BooksInstanceInline] 
admin.site.register(Book)   
admin.site.register(BookInstance)  
admin.site.register(Genre)

# Register your models here.
