from django.shortcuts import render
from bin.models import dustbin
from django.http import HttpResponse


# Create your views here.
def loopmarker(request):
    
    bins = dustbin.objects.all()
   
    return render(request,'maptest.html',bins)

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


