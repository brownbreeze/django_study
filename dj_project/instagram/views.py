from django.shortcuts import render
from .models import Post

def post_list(request):
    # request.GET
    # request.REQUEST
    # request.POST
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    # instagram/templates/instagram/post_list.html 를 암시
    return render(request, 'instagram/post_list.html',{
        'post_list' : qs,
        'q' : q,
    })
