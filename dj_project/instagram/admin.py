from django.contrib import admin
from .models import Post, Comment
from django.utils.safestring import mark_safe


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message'] # link 설정
    search_fields = ['message'] # 검색 쉽게 가능 
    list_filter = ['created_at', 'is_public'] # 데이터베이스 창 오른쪽에 필터 정보

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width:72px"/>')
        return None

    def message_length(self, post):
        return f'{len(post.message)} 글자'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass