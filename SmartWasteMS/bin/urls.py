from django.contrib import admin
from django.urls import path,include
from trashcan.views import home
from bin.views import bin_update,BinCreateView,display_dustbins,delete_dustbin,route_view,update_dustbin_data,AreaCreateView,StreetCreateView,status,download
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('bin_update/<int:bin_id>/<int:bin_status>',bin_update),
    path('add_bin/',BinCreateView.as_view(),name='create_dustbin'),
    path('bin_list/',display_dustbins,name='display_bins'),
    path('delete_bin/<int:bin_id>/',delete_dustbin,name='delete_bins'),
    path('update_dustbin_data/<int:bin_no>/',update_dustbin_data,name="update_dustbin_data"),
    path('route/<str:area>/',route_view,name='route'),
    path('add_area',AreaCreateView.as_view(),name='create_area'),
    path('add_street',StreetCreateView.as_view(),name='create_street'),
    path('status/',status,name='status'),
    path('download_proposal/',download,name='download_proposal'),


    
    

   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
