from django.contrib.auth.models import User
from django.forms import *

from zoo.models import Account


class ExcursionForm(Form):
    date = DateField(widget=DateInput(attrs={
        'type': 'date',
        'class': 'inputBox',
        'required': 'required'
    }))

    time = TimeField(widget=TimeInput(attrs={
        'type': 'time',
        'class': 'inputBox',
        'required': 'required',
        'min': '10:00',
        'max': '18:00'
    }))
    name = Field(widget=TextInput(attrs={
        'type': 'text',
        'class': 'inputBox',
        'required': 'required',
        'id': 'name'
    }))
    phone = Field(widget=TextInput(attrs={
        'type': 'tel',
        'class': 'inputBox',
        'required': 'required',
        'id': 'phone'
    }))
    peopleAmount = IntegerField(widget=NumberInput(attrs={
        'type': 'number',
        'class': 'inputBox',
        'required': 'required',
        'id': 'peopleAmount',
        'min': '5',
        'max': '20'
    }))
    guide = ModelChoiceField(queryset=Account.objects.filter(user__groups__name="Guide"))
