from django.shortcuts import render, redirect
from bin.models import dustbin
from django.views import View
from accounts.forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def success(request):
    template_name='accounts/success.html'
    return render(request, template_name)


@login_required
def userprofile(request):
    bins = dustbin.objects.all()

    template_name='index.html'
    return render(request,template_name,{'bins':bins})

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
