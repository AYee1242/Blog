from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from.models import Author, Tag, Post, Comment


class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "date")
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("username", "text", "post")


# Register your models here.
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
