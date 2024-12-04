from django import forms
from .models import Proyecto
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ProyectoForm(forms.ModelForm):
    class Meta:
        model =Proyecto
        fields = ['nombre_proyecto', 'rut', 'primer_nombre', 'segundo_apellido']
        widgets = {
            'nombre_proyecto': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar'))
