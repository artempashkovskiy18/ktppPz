from django.forms import ModelForm, DateInput, TimeInput, TextInput, NumberInput

from zoo.models import Excursions


class ExcursionForm(ModelForm):
    class Meta:
        model = Excursions
        fields = ['date', 'time', 'phone', 'peopleAmount', 'name']
        widgets = {
            'date': DateInput(attrs={
                'type': 'date',
                'class': 'inputBox',
                'required': 'required'
            }),
            'time': TimeInput(attrs={
                'type': 'time',
                'class': 'inputBox',
                'required': 'required',
                'min': '10:00',
                'max': '18:00'
            }),
            'name': TextInput(attrs={
                'type': 'text',
                'class': 'inputBox',
                'required': 'required',
                'id': 'name'
            }),
            'phone': TextInput(attrs={
                'type': 'tel',
                'class': 'inputBox',
                'required': 'required',
                'id': 'phone'
            }),
            'peopleAmount': NumberInput(attrs={
                'type': 'number',
                'class': 'inputBox',
                'required': 'required',
                'id': 'peopleAmount',
                'min': '5',
                'max': '20'
            })
        }
