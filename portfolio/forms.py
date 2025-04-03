from django.forms import Select, ModelForm, NumberInput, TextInput, CharField, URLInput, Textarea, FileInput
from . import models

class PortfolioForm(ModelForm):
    class Meta:
        model = models.Portfolio
        fields = ['name', 'surname', 'description', 'photo', 'ins', 'github', 'linkedin']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ім`я'}),
            'surname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Прізвище'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Розкажіть про себе'}),
            'photo': FileInput(attrs={'class': 'form-control rounded-circle border', 'style': 'width: 150px; height: 150px; object-fit: cover;', 'placeholder': 'Твоє фото'}),
            'ins': URLInput(attrs={'class': 'form-control', 'placeholder': 'Посилання на твій Instagram'}),
            'github': URLInput(attrs={'class': 'form-control', 'placeholder': 'Посилання на твій Github'}),
            'linkedin': URLInput(attrs={'class': 'form-control', 'placeholder': 'Посилання на твій LinkedIn'}),
        }
        
