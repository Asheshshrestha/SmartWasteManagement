from django.shortcuts import render, redirect,get_object_or_404
from bin.models import dustbin
from bin.forms import RouteSelect
from django.views import View
from accounts.forms import SignUpForm,Task_record
from django.core.paginator import Paginator
from django.conf import settings
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
from django.core.mail import send_mail
from accounts.email_data import DOMAIN
from trashcan.settings import ALLOWED_HOSTS
from datetime import datetime
from notifications.models import Notification
from notifications.utils import id2slug, slug2id
from notifications.signals import notify
from django.db.models import Q




# Create your views here.

def success(request):
    template_name='accounts/success.html'
    return render(request, template_name)

#========================================================================================
@login_required
def userprofile(request):
    u_form = Task_record(request.POST)

    if request.method =="POST":
        print("ashesh")
        u_form = Task_record(request.POST)
        
        if u_form.is_valid():
            user_obj= u_form.save(commit=False)
            user_obj.user=request.user
            user_obj.date_time= datetime.now()
            area= u_form.cleaned_data["area"]
            
            user_obj.save()
            print(area)
            return redirect("/route/"+str(area))
        else:
            u_form=Task_record(request.POST)

    bins = dustbin.objects.all()
    user = User.objects.get(pk=request.user.pk)
    notice = user.notifications.unread()
    domain = DOMAIN
    site = ALLOWED_HOSTS

    template_name='index.html'
    return render(request,template_name,{'bins':bins,'domain':domain,'site':site,'u_form':u_form,'notice':notice})
#=====================================================================================
@login_required
def notice_display(request):
    user = User.objects.get(pk=request.user.pk)
    notice_unread = user.notifications.unread()
    notice_read = user.notifications.read()
    context = {
        'notice_unread':notice_unread,
        'notice_read':notice_read,
    }
   
    template_name= 'notification/notice.html'
    return render(request,template_name,context)


        
#=====================================================================================
@login_required
def display_users(request):

    user_obj=User.objects.all()
    query = request.GET.get("q")
    if query:
        user_obj= user_obj.filter(
            Q(username__icontains=query) |
            Q(email__icontains=query) 
            ).distinct()
    paginator = Paginator(user_obj, 6) # Show 6 user per page
    page = request.GET.get('page')
    user = paginator.get_page(page)
    template_name = 'accounts/user_list.html'
    return render(request, template_name ,{'user':user})
            

#==============================================================================

def delete_user(request,username):
    user = User.objects.all()
    template_name='accounts/delete_success.html'
    for i in user:
        if i.username == username:
            i.delete()
    
    return render(request,template_name)

#=====================================================================================

def delete_user_confirm(request,username):
    username=username
    user = User.objects.all()

    template_name = 'accounts/delete_user_confirm.html'

    context={
        'username':username,
        'user' : user
    }

    return render(request,template_name,context)



#===================================================================================
def inactive_user(request,username):
    username= username
    user= User.objects.all()
    template_name = 'accounts/inactive_user_success.html'
    for i in user:
        if i.username == username:
            if i.is_active == True:
                i.is_active = False
            else:
                i.is_active = True
            i.save()
    
    return render(request,template_name)
#===================================================================================
def inactive_user_confirm(request,username):
    username=username
    user = User.objects.all()

    template_name = 'accounts/inactive_user_confirm.html'

    context={
        'username':username,
        'user' : user
    }
    return render(request,template_name,context)

#===================================================================================
@login_required
def userprofile_display(request):
    template_name='accounts/profile_display.html'
    return render(request,template_name)
#===================================================================================
@login_required
def update_profile(request):
    user= User.objects.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = CreateUserProfile(request.POST,
                                    request.FILES,
                                    instance= request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your accounts has been updated!')
            return redirect('profile_display')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = CreateUserProfile(instance= request.user.userprofile)

    context={
        'u_form':u_form,
        'p_form':p_form,
        'user':user,
    }
    return render(request,'accounts/update_profile.html',  context)
#========================================================================================
@login_required
def update_user_profile(request,username):
    user= User.objects.all()
    for i in user:
        if i.username == username:

            if request.method == 'POST':
                u_form = UserUpdateForm(request.POST,instance=i)
                p_form = CreateUserProfile(request.POST,
                                            request.FILES,
                                            instance= i.userprofile)
                if u_form.is_valid() and p_form.is_valid():
                    u_form.save()
                    p_form.save()
                    messages.success(request,f'Your accounts has been updated!')
                    return redirect('profile')

            else:
                u_form = UserUpdateForm(instance=i)
                p_form = CreateUserProfile(instance= i.userprofile)

            context={
                'u_form':u_form,
                'p_form':p_form,
                'user':user,
                'i':i,
            }
            return render(request,'accounts/update_user_profile.html',  context)
#========================================================================================
def reset_user_password(request,username):
    user_obj = User.objects.get(username=username)
    template_name = 'accounts/reset_user_password.html'
    if request.method == 'POST':
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(password1)
        if password1 == password2:
            print("ashesh")
            user_obj.set_password(password1)
            user_obj.save()
            messages.success(request,'Password has been changed successfully!')
            subject = "Password Reset"
            from_email = settings.EMAIL_HOST_USER
            to_mail = [user_obj.email]
            signup_message = """ Wellcome to TrashCan SmartWaste management system. To configure you profile please visit http://127.0.0.1:8080/login \nUsername:"""+username+"""\nPassword:"""+password1+"""Dear"""+username+""",\nYour password has been changed by admin("""+request.user.username+""") now you can sign in you account easyily . \n Thank you """
            send_mail(subject = subject,from_email=from_email,recipient_list=to_mail,message=signup_message,fail_silently=False)
            
        else:
            messages.error(request,'Password doesnot match!')
    return render(request,template_name,{'user_obj':user_obj})#========================================
        
#========================================================================================
class SignUpView(View):
    
    def get(self, request, *args, **kwargs):
        template_name='accounts/signup.html'
        form = SignUpForm()
        return render(request,template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        #value = {'username':"",'email':"",'first_name':"",'last_name':"",'password1':"Ashesh1234",'password2':"Ashesh1234"}
        form = SignUpForm(request.POST)
        template_name='accounts/success.html'
        if form.is_valid():
            user =form.save(commit=False)
            raw_password = form.cleaned_data['password1']
            #raw_password =  User.objects.make_random_password(length=8, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889!@#$%^&*")
            username = form.cleaned_data['username']
            user.set_password(raw_password)
            user.save()
            subject = "Congratulation you are Inside the Trashcan Board"
            from_email = settings.EMAIL_HOST_USER
            to_mail = [user.email]
            signup_message = """ Wellcome to TrashCan SmartWaste management system. To configure you profile please visit http://127.0.0.1:8080/login \nUsername:"""+username+"""\nPassword:"""+raw_password
            send_mail(subject = subject,from_email=from_email,recipient_list=to_mail,message=signup_message,fail_silently=False)


            return redirect('/success/')

        else:
            return render(request, 'accounts/signup.html', {'form':form})



@login_required
def mark_as_read_notice(request, slug=None):
    notification_id = slug2id(slug)

    notification = get_object_or_404(
        Notification, recipient=request.user, id=notification_id)
    notification.mark_as_read()

    _next = request.GET.get('next')

    if _next:
        return redirect(_next)

    return redirect('/noticelist')



