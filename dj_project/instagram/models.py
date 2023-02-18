from django.db import models
#from django.contrib.auth.models import User  
# django 는 유동적이기 때문에 위 방법은 추천하지 않음
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    # upload_to 변경 시, file 올릴 경우에 반영 
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y%m%d') 
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # java의 toString
    def __str__(self):
        #return f'Custom Post object({self.id})'
        return self.message
        
    class Meta:
        ordering = ['-id']

    def message_length(self):
        return len(self.message)
    # model 단에서 구현하느나, admin 단에서 구현하느냐..? 
    # 자주 쓰이는 것은 model 단이 맞을 것 같다.
    message_length.short_description = '메시지 글자수'

# 모델명 충돌 가능 
class Comment(models.Model):
    # 외래키 생성
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                                limit_choices_to={'is_public':True}) # instagram 안에서 Post를 찾아감
    # CASCADE 는 Post를 삭제하면 Comment도 삭제됨
    # post = models.ForeignKey('instagram.Post', on_delete=models.CASCADE) # 다른 app을 통해 찾아갈 경우
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)