from django.forms import Select, ModelForm, NumberInput, TextInput
from . import models

class MarkForm(ModelForm):
    class Meta:
        model = models.Mark
        fields = ['student', 'subject', 'mark']
        widgets = {
            'student': Select(attrs={'class': 'form-control'}),
            'subject': Select(attrs={'class': 'form-control'}),
            'mark': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Оцінка'}),
        }
        
