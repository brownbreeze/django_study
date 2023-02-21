from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),
    # path('archives/<int:year>/', views.archives_year),
    # 특정 연도 또는 4자리 숫자만 허용하고 싶을 경우,
    # ?P python re 작성법
    re_path(r'archives/(?P<year>\d{4})/', views.archives_year),
]