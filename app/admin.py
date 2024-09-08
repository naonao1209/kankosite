from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'image')
    search_fields = ('title', 'text')

admin.site.register(Post, PostAdmin)