from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ArchiveIndexView, ListView, YearArchiveView
from .forms import PostForm
from .models import Post


def post_new(request):
    form = PostForm()
    return render(request, 'instagram/post_form.html',{
        'form':form,        
    })

# view 기준이나, 이는 function 을 더 익숙하게 한 후 사용 권장 
# post_list = login_required(ListView.as_view(model=Post, paginate_by=10))
# 요즘방식
#class PostListVipew(LoginRequiredMixin, ListView):
# dispatch 란 class 기반 뷰에서 실제 요청왔을 때, 
# 어떤 request method function이 호출된다 하더라도 호출되는 function
@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    paginate_by = 10

post_list = PostListView.as_view()

# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     # instagram/templates/instagram/post_list.html 를 암시
#     return render(request, 'instagram/post_list.html',{
#         'post_list' : qs,
#         'q' : q,
#     })

# def post_detail(request: HttpRequest, pk: int) -> HttpResponse: 
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html',{
#         'post':post,
#     })

# 관례에 맞게 개발할경우, 이렇게 소스 양이 작아짐 
post_detail = DetailView.as_view(model=Post)


# def archives_year(request, year):
#     return HttpResponse(f"{year}년")

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at',
    paginate_by=10)

post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)
