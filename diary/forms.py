from django.forms import Select, ModelForm, NumberInput, TextInput
from . import models

class MarkForm(ModelForm):
    class Meta:
        model = models.Mark
        fields = ['student', 'subject', 'mark']
        widgets = {
            'student': Select(attrs={'class': 'form-control'}),
            'subject': TextInput(attrs={'class': 'form-control', 'placeholder': 'За що оцінка'}),
            'mark': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Оцінка'}),
        }
        
