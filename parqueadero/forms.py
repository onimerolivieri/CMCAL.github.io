from django import forms
from .models import Vehiculo, Funcionario

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['propietario', 'placas', 'marca', 'color', 'esta_autorizado'] 

class BuscarVehiculoForm(forms.Form):
    placa = forms.CharField(max_length=20, required=True)

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nombre', 'lugar_trabajo', 'cargo', 'documento']

