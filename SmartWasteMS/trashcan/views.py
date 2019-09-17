from django.shortcuts import render
from bin.models import dustbin
from blogs.models import Blogs
from accounts.email_data import DOMAIN

def home(request):
    blogs=Blogs.objects.all()
    template_name='maptest.html'
    return render(request,template_name,{'blogs':blogs})



