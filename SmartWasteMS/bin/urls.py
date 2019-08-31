from django.contrib import admin
from django.urls import path,include
from trashcan.views import home
from . import views

urlpatterns = [
    path('bin_update/<int:bin_id>/<int:bin_status>', views.bin_update),
]
