from django import forms
from .models import Tienda1, Tienda2, Tienda3, Tienda4, Tienda5



#--------------------------------Tienda 1---------------------#
class Tienda1Form(forms.ModelForm):
    class Meta:
        model = Tienda1
        fields = ('numero_tienda', 'layer_code', 'fecha_ingreso')
        


#--------------------------------Tienda 2---------------------#
class Tienda2Form(forms.ModelForm):
    class Meta:
        model = Tienda2
        fields = ['numero_tienda', 'layer_code', 'fecha_ingreso']
        
#--------------------------------Tienda 3---------------------#   
class Tienda3Form(forms.ModelForm):
    class Meta:
        model = Tienda3
        fields = ['numero_tienda', 'layer_code', 'fecha_ingreso']
        
#--------------------------------Tienda 4---------------------#       
class Tienda4Form(forms.ModelForm):
    class Meta:
        model = Tienda4
        fields = ['numero_tienda', 'layer_code', 'fecha_ingreso']
        
        
#--------------------------------Tienda 5---------------------#  
class Tienda5Form(forms.ModelForm):
    class Meta:
        model = Tienda5
        fields = ['numero_tienda', 'layer_code', 'fecha_ingreso']