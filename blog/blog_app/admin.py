from django.contrib import admin
from .models import Post
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.utils.html import format_html

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'status', 'display_image_thumbnail')

    def display_image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return ''

    display_image_thumbnail.short_description = 'Image'  # Set a user-friendly column header for the image

admin.site.register(Post, PostAdmin)