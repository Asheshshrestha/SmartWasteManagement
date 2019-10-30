from django.shortcuts import render
from bin.models import dustbin

from accounts.email_data import DOMAIN

def home(request):
    
    template_name='maptest.html'
   
    return render(request,template_name)



