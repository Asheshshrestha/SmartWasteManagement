from django.shortcuts import render
from bin.models import dustbin

def home(request):
    bins = dustbin.objects.all()
    template_name='maptest.html'
    return render(request,template_name,{'bins':bins})


