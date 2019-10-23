from django.shortcuts import render,redirect
from bin.models import dustbin,Area,street
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic.edit import CreateView
from bin.forms import AddNewDustbin,UpdateDustbin,Add_AreaForm,Add_StreetForm
from django.views.generic import View
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q
from notifications.signals import notify
from django.contrib.auth.models import User






# Create your views here.

class BinCreateView(LoginRequiredMixin,CreateView):
    bins = dustbin.objects.all()
    
    model = dustbin
    template_name = "dustbin/dustbincreate.html"
    
    form_class = AddNewDustbin
    success_url = '/profile/'
    
    def form_valid(self,form):
        user = User.objects.all()
        bin = form.save(commit=False)
        bin.added_by = self.request.user
        bin.bin_logitude=self.request.POST.get("bin_logitude")
        bin.bin_latitude=self.request.POST.get("bin_latitude")

        bin.save()
        notify.send(self.request.user, recipient=user, verb=' added new dustbin',action_object=self.request.user,description='ID:'+'N\A'+ '\nLocation:')
                                                 

        return super().form_valid(form)

    def form_invalid(self,form):
        print(form)
        return super(AddNewDustbin,self).form_invalid(form)

    
#======================================================================================
class AreaCreateView(LoginRequiredMixin,CreateView):
    model = Area
    user = User.objects.all()

    template_name = "dustbin/add_area.html"
    form_class = Add_AreaForm
    success_url = '/bin_list/'
    def form_valid(self,form):
        area = form.save(commit=False)
        area.area_logitude=self.request.POST.get("area_logitude")
        area.area_latitude=self.request.POST.get("area_latitude")
        area.save()
        notify.send(self.request.user, recipient=user, verb=' added new Area',action_object=self.request.user,description='ID:'+'N\A'+ '\nLocation:')

        return super().form_valid(form)
    def form_invalid(self,form):
        print(form)
        return super(Add_AreaForm,self).form_invalid(form)
        
#======================================================================================
class StreetCreateView(LoginRequiredMixin,CreateView):
    model = street
    user = User.objects.all()

    template_name = "dustbin/add_street.html"
    form_class =Add_StreetForm
    success_url = '/bin_list/'
    def form_valid(self,form):
        street_name=form.save(commit=False)
        street_name.save()
        notify.send(self.request.user, recipient=user, verb=' added new Street',action_object=self.request.user,description='ID:'+'N\A'+ '\nLocation:')

        return super().form_valid(form)
    def form_invalid(self,form):
        print(form)
        return super(Add_StreetForm,self).form_invalid(form)
        
#======================================================================================
@login_required
def update_dustbin_data(request,bin_no):
    bin_no=bin_no
    bin = dustbin.objects.get(bin_no=bin_no)
    u_form = UpdateDustbin(request.POST or None,instance=bin)

   
    if request.method =='POST':
        u_form = UpdateDustbin(request.POST,instance=bin)

        bin.updated_by =request.user
        bin.bin_logitude=request.POST.get("bin_logitude")
        bin.bin_latitude=request.POST.get("bin_latitude")
        if u_form.is_valid():
            u_form.save()
            bin.save()
            return redirect('/bin_list/')
        else:
            u_form = UpdateDustbin(instance= bin)
            
    context={
                'u_form':u_form,
                'bin_no':bin_no,
                'lnga':bin.bin_logitude,
                'lata':bin.bin_latitude,

            }
    return  render(request,'dustbin/update_dustbin.html',context)             

#======================================================================================

@login_required
def display_dustbins(request):
    

    bins_obj=dustbin.objects.all()
    query = request.GET.get("q")
    if query:
        bins_obj = bins_obj.filter(
            Q(bin_no__icontains=query) |
            Q(bin_area__area_name__icontains=query) |
            Q(bin_street__street_name__icontains=query) |
            Q(added_by__username__icontains=query)
            ).distinct()
    paginator = Paginator(bins_obj, 7) # Show 7 user per page
    page = request.GET.get('page')
    bins = paginator.get_page(page)

    template_name = 'dustbin/dustbin_list.html'
    return render(request, template_name ,{'bins':bins})
          

#======================================================================================

def delete_dustbin(request,bin_id):
    bins = dustbin.objects.all()
    bin_id=bin_id
    user = User.objects.all()

    template_name='dustbin/delete_success.html'
    for i in bins:
        if i.bin_no == int(bin_id):
            
            notify.send(request.user, recipient=user, verb=' deleted dustbin',action_object=request.user,description='ID:'+str(i.bin_no)+'\nLocation:')
            i.delete()
    
    return render(request,template_name)
#======================================================================================


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

#==========================================================================================

def route_view(request,area):
    user = User.objects.all()
    bins = dustbin.objects.filter(bin_area__area_name__icontains=area)
    template_name='dustbin/pick_route.html'
    cord=[]
    for i in bins:
        if( i.bin_status <= 30):
            cord.append(i)
    notify.send(request.user, recipient=user, verb=' Checked out the bins of '+str(area),action_object=request.user,description='Area:'+str(area))
           
    return render(request,template_name,{'cord':cord})

#============================================================================================

#============================================================================================



