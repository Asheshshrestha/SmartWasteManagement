from django.contrib import admin
from django.urls import path,include
from trashcan.views import home
from bin.views import bin_update,BinCreateView,display_dustbins,delete_dustbin,route_view,update_dustbin_data

urlpatterns = [
    path('bin_update/<int:bin_id>/<int:bin_status>',bin_update),
    path('add_bin/',BinCreateView.as_view(),name='create_dustbin'),
    path('bin_list/',display_dustbins,name='display_bins'),
    path('delete_bin/<int:bin_id>/',delete_dustbin,name='delete_bins'),
    path('update_dustbin_data/<int:bin_no>/',update_dustbin_data,name="update_dustbin_data"),
    path('route/',route_view,name='route'),

   

]
