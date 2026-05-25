from django import forms
from django.forms import ModelForm
from servicio.models import Servicio,Detalle_servicio
from usuarios.models import Usuario

class ServicioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'nombres' in self.fields:
            self.fields['nombres'].queryset = Usuario.objects.filter(
                tipo_usuario__iexact=Usuario.TipoUsuario.MECANICO,
                estado=Usuario.Estado.ACTIVO,
            )

    class Meta:
        model = Servicio
        fields = "__all__"
       
       
class ServicioUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'nombres' in self.fields:
            self.fields['nombres'].queryset = Usuario.objects.filter(
                tipo_usuario__iexact=Usuario.TipoUsuario.MECANICO,
                estado=Usuario.Estado.ACTIVO,
            )

    class Meta:
        model = Servicio
        fields = "__all__"
        
        
class Detalle_servicioForm(ModelForm):
    class Meta:
        model = Detalle_servicio
        fields = "__all__"
    

class Detalle_servicioUpdateForm(ModelForm):
    
    class Meta:
        model = Detalle_servicio
        fields = "__all__"
 
  