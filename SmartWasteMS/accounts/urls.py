from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView,PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView
from accounts.views import SignUpView,update_profile,userprofile_display,update_user_profile,reset_user_password,notice_display,mark_as_read_notice
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('success/', views.success, name='success'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('createuser/', SignUpView.as_view(), name='signup'),
    path('profile/',views.userprofile,name='profile'),
    path('update_profile/',update_profile,name='update_profile'),
    path('update_user_profile/<str:username>/',update_user_profile,name='update_user_profile'),
    path('profile_display/',userprofile_display,name='profile_display'),
    path('user_list/',views.display_users,name='user_list'),
    path('user_delete/<str:username>/',views.delete_user,name='user_delete'),
    path('user_delete_confirm/<str:username>/',views.delete_user_confirm,name='delete_user_confirm'),
    path('user_suspend/<str:username>/',views.inactive_user,name="inactive_user"),
    path('user_suspend_confirm/<str:username>/',views.inactive_user_confirm,name='inactive_user_confirm'),
    path('noticelist/',notice_display,name='notice_display'),
    path('mark_as_read_notice/(?P<slug>\d+)/$',mark_as_read_notice,name='mark_as_read_notice'),
    path('password-reset/',
         PasswordResetView.as_view(
             template_name='accounts/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_conform.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('reset-user-password/<str:username>/',reset_user_password,name='reset-user-password'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
