from django.contrib import admin
from blog.models import Blogs


@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "text", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title", "text")
