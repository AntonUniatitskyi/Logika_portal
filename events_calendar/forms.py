from django.forms import Select, ModelForm, NumberInput, DateInput, TimeInput, TextInput
from . import models

class EventForm(ModelForm):
    class Meta:
        model = models.Event
        fields = ['subject','group','description','date','start_time']
        widgets = {
            'group': Select(attrs={'class': 'form-control'}),
            'subject': Select(attrs={'class': 'form-control'}),
            'date':DateInput(attrs={'class': 'form-control','placeholder': 'Дата'}),
            'start_time':TimeInput(attrs={'class': 'form-control','placeholder': 'Час початку'}),
            'description':TextInput(attrs={'class': 'form-control','placeholder': 'Домашнє завдання'}),
        }
        
