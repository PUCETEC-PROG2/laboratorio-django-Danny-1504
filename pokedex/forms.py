from django import forms
from models import Pokemon

class pokemonform(forms.ModelForm):
    class Meta:
        model = Pokemon 
        fields = '__all__'