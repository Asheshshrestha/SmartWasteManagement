from django import forms
from bin.models import dustbin,Area,street

class AddNewDustbin(forms.ModelForm):
    class Meta:
        model = dustbin
        fields=["bin_no","bin_area","bin_street","assigned_user"]

class UpdateDustbin(forms.ModelForm):
    class Meta:
        model = dustbin
        fields = ["bin_area","bin_street"]


class RouteSelect(forms.ModelForm):
    class Meta:
        model = Area
        fields = ["area_name"]


class Add_AreaForm(forms.ModelForm):
    
    class Meta:
        model = Area
        fields = ["area_name","assigned_user"]

class Add_StreetForm(forms.ModelForm):
    
    class Meta:
        model = street
        fields = ("street_name","street_area","assigned_user")
  