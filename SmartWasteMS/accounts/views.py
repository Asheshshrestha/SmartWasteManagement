from django.shortcuts import render, redirect
from bin.models import dustbin
from django.views import View
from accounts.forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from accounts.models import UserProfile
from accounts.forms import CreateUserProfile,UserUpdateForm
from django.views.generic.edit import CreateView
from django.contrib import messages
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound




# Create your views here.

def success(request):
    template_name='accounts/success.html'
    return render(request, template_name)


@login_required
def userprofile(request):
    bins = dustbin.objects.all()

    template_name='index.html'
    return render(request,template_name,{'bins':bins})

@login_required
def display_users(request):
    if request.user.is_superuser:

        user=User.objects.all()
        template_name = 'accounts/user_list.html'
        return render(request, template_name ,{'user':user})
    else:
        return HttpResponseNotFound()         





#===================================================================================
@login_required
def userprofile_display(request):
    template_name='accounts/profile_display.html'
    return render(request,template_name)
#===================================================================================
@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = CreateUserProfile(request.POST,
                                    request.FILES,
                                    instance= request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your accounts has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = CreateUserProfile(instance= request.user.userprofile)

    context={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'accounts/update_profile.html',  context)
#========================================================================================
class SignUpView(View):
    
    def get(self, request, *args, **kwargs):
        template_name='accounts/signup.html'
        form = SignUpForm()
        return render(request,template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        template_name='accounts/success.html'
        if form.is_valid():
            user =form.save(commit=False)
            raw_password = form.cleaned_data['password1']
            username = form.cleaned_data['username']
            user.set_password(raw_password)
            user.save()

            return redirect('/success/')

        else:
            return render(request, 'accounts/signup.html', {'form':form})
