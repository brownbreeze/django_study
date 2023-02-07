from django.contrib import admin
from .models import Post

# 1 
#admin.site.register(Post)

# 2
# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin)

# 3
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message'] # link 설정
    search_fields = ['message'] # 검색 쉽게 가능 
    list_filter = ['created_at', 'is_public'] # 데이터베이스 창 오른쪽에 필터 정보

    def message_length(self, post):
        return f'{len(post.message)} 글자'
