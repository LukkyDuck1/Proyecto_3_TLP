from django import forms 
from .models import RegistroProduccion

class RegistroProduccionForm(forms.ModelForm):
    class Meta:
        model = RegistroProduccion
        fields = ['producto', 'planta', 'cantidad', 'fecha_produccion', 'turno']
        widgets = {
            'fecha_produccion': forms.DateInput(attrs={'type': 'date'}),
            'turno': forms.Select(attrs={'class': 'form-control'}),
        }  