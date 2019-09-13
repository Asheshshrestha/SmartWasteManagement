from django import forms
from bin.models import dustbin

class AddNewDustbin(forms.ModelForm):
    class Meta:
        model = dustbin
        fields=["bin_no","bin_area","bin_street","bin_logitude","bin_latitude"]