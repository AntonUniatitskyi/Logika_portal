<<<<<<< HEAD
from django.forms import Select, ModelForm, NumberInput, DateInput, TimeInput, TextInput
=======
from django.forms import Select, ModelForm, NumberInput, DateInput, TimeInput
>>>>>>> 4653137 (new visual functionality)
from . import models

class EventForm(ModelForm):
    class Meta:
        model = models.Event
        fields = ['subject','group','description','date','start_time']
        widgets = {
            'group': Select(attrs={'class': 'form-control'}),
            'subject': Select(attrs={'class': 'form-control'}),
<<<<<<< HEAD
            'date':DateInput(attrs={'class': 'form-control','placeholder': 'Дата'}),
            'start_time':TimeInput(attrs={'class': 'form-control','placeholder': 'Час початку'}),
            'description':TextInput(attrs={'class': 'form-control','placeholder': 'Домашнє завдання'}),
=======
            'date':DateInput(atts={'class': 'form-control','placeholder': 'Дата'}),
            'start_time':TimeInput(atts={'class': 'form-control','placeholder': 'Час початку'}),
            'mark': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Оцінка'}),
>>>>>>> 4653137 (new visual functionality)
        }
        
