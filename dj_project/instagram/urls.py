from django.urls import path, include #, re_path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),
#    re_path(r'(?P<pk>\)/$', views.post_detail),
]