from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import SignUpView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('success/', views.success, name='success'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('createuser/', SignUpView.as_view(), name='signup'),
    path('profile/',views.userprofile,name='profile')


]
