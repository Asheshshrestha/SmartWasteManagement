from django import forms
from bin.models import dustbin,Area

class AddNewDustbin(forms.ModelForm):
    class Meta:
        model = dustbin
        fields=["bin_no","bin_area","bin_street"]

class UpdateDustbin(forms.ModelForm):
    class Meta:
        model = dustbin
        fields = ["bin_no","bin_area","bin_street"]


class RouteSelect(forms.ModelForm):
    class Meta:
        model = Area
        fields = ["area_name"]