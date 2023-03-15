from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render 
from accounts.forms import ProfileForm
from accounts.models import Profile 

# def profile(request):
#     return render(request, 'accounts/profile.html')

from django.views.generic import TemplateView, UpdateView

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    
profile = ProfileView.as_view()


# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = Profile
#     form_class = ProfileForm

# profile_edit = ProfileUpdateView.as_view()

@login_required
def profile_edit(request):
    # profile = request.user.profile
    #위와 같은 코드
    # #    Profile.objects.get(user=request.user)
    try :
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # user 재정의 추가 
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    
    return render(request, 'accounts/profile_form.html', {
        'form':form,
    })