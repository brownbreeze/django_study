from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ArchiveIndexView, ListView, YearArchiveView, CreateView, UpdateView, DeleteView
from .forms import PostForm 
from .models import Post

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    def form_valid(self, form):
        return super().form_valid(form)

post_edit = PostUpdateView.as_view()

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, '포스팅을 저장했습니다.')
        
        return super().form_valid(form)

post_new = PostCreateView.as_view()

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
    
#     # 작성자 check tip 
#     if post.author != request.user :
#         # 장식자를 이용해서 적용 가능 
#         messages.error(request, '작성자만 수정할 수 있습니다.')
#         return redirect(post) 

#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid(): # 유효성 검증 
#             post = form.save()
#             messages.success(request, '포스팅을 수정했습니다.')

#             return redirect(post)
#     else:
#         form = PostForm(instance=post)
        
#     return render(request, 'instagram/post_form.html',{
#         'form':form,        
#     })
    

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # TODO 
    if request.method =='POST':
        post.delete()
        messages.success(request, '포스팅을 삭제했습니다.')
        return redirect('instagram:post_list')
    return render(request, 'instagram/post_confirm_delete.html',{
        'post' : post,
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
        
#     messages.info(request, 'message 테스트')
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

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model =Post 
    success_url = reversed('instagrem')
    
    def get_success_url(self):
        return reversed('instagram:post_list')
     
# 관례에 맞게 개발할경우, 이렇게 소스 양이 작아짐 
post_detail = DetailView.as_view(model=Post)


post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at',
    paginate_by=10)

post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)
