from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'text', 'create_time']


admin.site.register(Comment , CommentAdmin)
