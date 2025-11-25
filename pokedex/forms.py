from django import forms
from .models import Pokemon,Trainer

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
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        labels = {
            "name_trainer": "Nombre del Entrenador",
            "lastname": "Apellido",
            "level": "Nivel",
            "birthdate": "Fecha de Nacimiento",
            "picture": "Foto del Entrenador"
        }
        widgets = {
            'name_trainer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa el nombre del entrenador'
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa el apellido del entrenador'
            }),
            'level': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '100',
                'placeholder': 'Nivel entre 1 y 100'
            }),
            'birthdate': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }
    
    def clean_level(self):
        level = self.cleaned_data.get('level')
        if level < 1 or level > 100:
            raise forms.ValidationError("El nivel debe estar entre 1 y 100")
        return level
    
    def clean_name_trainer(self):
        name_trainer = self.cleaned_data.get('name_trainer')
        if len(name_trainer) < 2:
            raise forms.ValidationError("El nombre debe tener al menos 2 caracteres")
        return name_trainer