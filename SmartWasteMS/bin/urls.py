from django.contrib import admin
from django.urls import path,include
from trashcan.views import home
from bin.views import bin_update,BinCreateView

urlpatterns = [
    path('bin_update/<int:bin_id>/<int:bin_status>',bin_update),
    path('add_bin/',BinCreateView.as_view(),name='create_dustbin'),
]
