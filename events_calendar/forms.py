from django.forms import Select, ModelForm, NumberInput, DateInput, TimeInput
from . import models

class EventForm(ModelForm):
    class Meta:
        model = models.Event
        fields = ['subject','group','description','date','start_time']
        widgets = {
            'group': Select(attrs={'class': 'form-control'}),
            'subject': Select(attrs={'class': 'form-control'}),
            'date':DateInput(atts={'class': 'form-control','placeholder': 'Дата'}),
            'start_time':TimeInput(atts={'class': 'form-control','placeholder': 'Час початку'}),
        }
        
