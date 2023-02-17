from django.db import models

class Post(models.Model):
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
