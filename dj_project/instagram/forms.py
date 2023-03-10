import re
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        # fields = '__all__'
        fields = [
            'message','photo','tag_set','is_public'
        ]
        # exclude = [ ] # 비추
    #   def clean() # 두개 이상의 유형에 대한 유효성 검사가 필요할 때 -> Form객체.clean()
    # From에서 수행하는 유효성검사 
    # 1. validator 2. Form 클래스 내 clean, clean_멤버함수를 통한 유효성검사 
    def clean_message(self): # 하나에 대한 유효성 검사가 필요할 때 
        message = self.cleaned_data.get('message')
        if message:
            message = re.sub(r'[a-zA-Z]+', '', message)
        return message