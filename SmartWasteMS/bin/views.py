from django.shortcuts import render
from bin.models import dustbin
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic.edit import CreateView
from bin.forms import AddNewDustbin
from django.views.generic import View



# Create your views here.

class BinCreateView(LoginRequiredMixin,CreateView):
    bins = dustbin.objects.all()
    
    model = dustbin
    template_name = "dustbin/dustbincreate.html"
    
    form_class = AddNewDustbin
    success_url = '/profile/'
    
    def form_valid(self,form):
        
        bin = form.save(commit=False)
        bin.added_by = self.request.user
        bin.save()
        return super().form_valid(form)

    def form_invalid(self,form):
        print(form)
        return super(AddNewDustbin,self).form_invalid(form)

    def loadmarker(request):
        bins = dustbin.objects.all()
        return render(request,template_name,{'bins':bins})





    

def bin_update(request,bin_id,bin_status):
    bin_id=bin_id
    bin_status=bin_status
    bins=dustbin.objects.all()

    for i in bins:
        if(i.bin_no == int(bin_id)):
            i.bin_status=int(bin_status)
            i.save()
            return HttpResponse("Updated Sucessfully")
    return HttpResponse("Cannot update")


