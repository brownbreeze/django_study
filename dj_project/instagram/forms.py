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
