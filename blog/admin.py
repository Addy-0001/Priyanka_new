from django.contrib import admin
from .models import Author, Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title', )}

admin.site.register(Author)
admin.site.register(Blog, BlogAdmin)
