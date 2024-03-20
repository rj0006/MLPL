# forms.py

from django import forms
from .models import Consignment

class ConsignmentForm(forms.ModelForm):
    class Meta:
        model = Consignment
        fields = ['consignment_no', 'consignment_date']
