from django import forms
from .models import Pokemon

class pokemonform(forms.ModelForm):
    class Meta:
        model = Pokemon 
        fields = '__all__'
        labels = {
            "name" : "Nombre",
            "type": "Tipo",
            "Heigth":"Altura",
            "weigth":"Peso",    
            "picture":"Foto"
            
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'Heigth': forms.NumberInput(attrs={'class': 'form-control'}),
            'weigth': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'})
       }