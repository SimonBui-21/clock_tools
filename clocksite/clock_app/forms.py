from django import forms
from .models import Shifts



class ShiftsForm(forms.ModelForm):
    class Meta:
        model = Shifts
        fields = ['created_by','start', 'end']

