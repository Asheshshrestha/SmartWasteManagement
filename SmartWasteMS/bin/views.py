from django.shortcuts import render,redirect
from bin.models import dustbin,Area,street,stat_count
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
from accounts.forms import Task_record
from datetime import datetime
from django.http import FileResponse,JsonResponse,HttpResponse







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
    

    template_name = "dustbin/add_area.html"
    form_class = Add_AreaForm
    success_url = '/bin_list/'
    def form_valid(self,form):
        user = User.objects.all()
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
        user = User.objects.all()

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
        if( i.bin_status >= 30):
            cord.append(i)
    notify.send(request.user, recipient=user, verb=' Checked out the bins of '+str(area),action_object=request.user,description='Area:'+str(area))
           
    return render(request,template_name,{'cord':cord})

#============================================================================================
@login_required
def status(request):
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
    user_active = User.objects.filter(is_active=True).count()
    user_inactive = User.objects.filter(is_active=False).count()
    t_area = Area.objects.all().count()


    n,f,h,e,t=bin_calculation()

    template_name='charts/status.html'
    data= {'Full Dustbin': f, 'Half Dustbin': h, 'Empty Dustbin': e,'Damaged Dustbin' : t,'New Dustbin':n}

    counts = stat_count.objects.all()[:6]
    full_list = []
    half_list = []
    empty_list = []
    for i in counts:
        full_list.append([str(i.date_time),i.full_bin])
        half_list.append([str(i.date_time),i.half_bin])
        empty_list.append([str(i.date_time),i.empty_bin])


    data_eff = [{'data': full_list, 'name': 'Full Dustbin'},
    {'data': empty_list, 'name': 'Empty Dustbin'},
    {'data': half_list, 'name': 'Half Dustbin'}]
    
    
    
    return render(request,template_name,{'data':data,'data_eff':data_eff,'f':f,'h':h,'e':e,'t':t,'u_form':u_form,'inactive_user':user_inactive,'active_user':user_active,'area_count':t_area})

#============================================================================================
def download(request):
    file_data = FileResponse(open('D:\Smart_Waste_management_system\Smart Waste Management System   (Autosaved).docx', 'rb'))
    return file_data

#====================================================================================================
def area_list_display(request):
    template_name = 'dustbin/area_list.html'
    area_obj = Area.objects.all()
    query = request.GET.get("q")
    if query:
        area_obj = area_obj.filter(
            Q(area_name__icontains=query) |
            Q(assigned_user__username__icontains=query)
            ).distinct()
    paginator = Paginator(area_obj, 7) # Show 7 user per page
    page = request.GET.get('page')
    area = paginator.get_page(page)

    return render(request,template_name,{'area':area})
#====================================================================================================
def street_list_display(request):
    template_name = 'dustbin/street_list.html'
    street_obj = street.objects.all()
    query = request.GET.get("q")
    if query:
        street_obj = street_obj.filter(
            Q(street_name__icontains=query) |
            Q(street_area__area_name__icontains=query) |
            Q(assigned_user__username__icontains=query)
            ).distinct()
    paginator = Paginator(street_obj, 7) # Show 7 user per page
    page = request.GET.get('page')
    streets = paginator.get_page(page)

    return render(request,template_name,{'streets':streets})


#====================================================================================================
def bin_calculation():
    bins= dustbin.objects.all()
    f=0
    h=0
    e=0
    t=0
    n=0
    for i in bins:
        if i.bin_status==-1:
            n=n+1
        elif i.bin_status>50:
            f=f+1
        elif i.bin_status>10:
            h=h+1
        elif i.bin_status>0:
            e = e+1
        else:

            t=t+1
    return n,f,h,e,t



