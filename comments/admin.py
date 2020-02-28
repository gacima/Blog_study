from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_time']  # 后台评论列表展示部分
    fields = ['name', 'email', 'url', 'text', 'post']  # 单个评论的编辑页面


admin.site.register(Comment, CommentAdmin)