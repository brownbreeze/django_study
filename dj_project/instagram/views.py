# from django.views.generic import ListView
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse, HttpRequest

# view 기준이나, 이는 function 을 더 익숙하게 한 후 사용 권장 
# post_list = ListView.as_view(model=Post)

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

def post_detail(request: HttpRequest, pk: int) -> HttpResponse: 
    #eturn render(request, 'instagram/post_list.html')
    # request.method, META, GET, POST, FILES, body
    response = HttpResponse()
    response.write("hello world")
    response.write("hello world")
    return response

def archives_year(request, year):
    return HttpResponse(f"{year}년")
