from django.contrib import admin
from socialApp import models

# Register your models here.
admin.site.register(models.Like)

class CommentInline(admin.TabularInline):
    model = models.Comment

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'normal_user', 'title', 'description', 'likes_count', 'created_at')
    inlines = [CommentInline,]

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'normal_user', 'text', 'post')