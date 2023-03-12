from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login_form.html'), name='login'),  
]