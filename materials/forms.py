from django.forms import Select, ModelForm, URLInput, TextInput
from . import models

class MaterialForm(ModelForm):
    class Meta:
        model = models.Materials
        fields = ['title', 'url']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control','placeholder': 'Назва'}),
            'url': URLInput(attrs={'class': 'form-control','placeholder': 'Посилання'}),
        }
        
