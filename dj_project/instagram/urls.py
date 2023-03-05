from django.urls import path, include, re_path, register_converter
from . import views
from .converters import YearConverter, MonthConverter, DayConverter
register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

app_name = 'instagram' # URL Reverse 에서 namespace 역할 

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    # path('archives/<int:year>/', views.archives_year),
    # path('archives/<year:year>/', views.archives_year),
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
    # path('archive/<year:year>/<month:month>', views.post_archive_month, name='post_archive_month'),
    # path('archive/ <year:year>/<month:month>/<day:day>', views.post_archive_day, name='post_archive_day'),
]