from datetime import date

from django.forms import ModelForm, DateInput, TimeInput, TextInput, NumberInput

from zoo.models import Excursions


class ExcursionForm(ModelForm):
    class Meta:
        model = Excursions
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExcursionForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'type': 'date',
                                                 'class': 'inputBox',
                                                 'required': 'required',
                                                 'min': date.today().strftime('%Y-%m-%d')})

        self.fields['time'].widget.attrs.update({'type': 'time',
                                                 'class': 'inputBox',
                                                 'required': 'required',
                                                 'min': '10:00',
                                                 'max': '18:00'})

        self.fields['name'].widget.attrs.update({'class': 'inputBox',
                                                 'required': 'required',
                                                 'id': 'name'})

        self.fields['phone'].widget.attrs.update({'type': 'tel',
                                                  'class': 'inputBox',
                                                  'required': 'required',
                                                  'id': 'phone'})

        self.fields['peopleAmount'].widget.attrs.update({'class': 'inputBox',
                                                         'required': 'required',
                                                         'id': 'peopleAmount',
                                                         'min': '5',
                                                         'max': '20'})

        self.fields['guide'].widget.attrs.update({'class': 'inputBox'})


    # class Meta:
    #     model = Excursions
    #     fields = ['date', 'time', 'phone', 'peopleAmount', 'name', 'guide']
    #     widgets = {
    #         'date': DateInput(attrs={
    #             'type': 'date',
    #             'class': 'inputBox',
    #             'required': 'required'
    #         }),
    #         'time': TimeInput(attrs={
    #             'type': 'time',
    #             'class': 'inputBox',
    #             'required': 'required',
    #             'min': '10:00',
    #             'max': '18:00'
    #         }),
    #         'name': TextInput(attrs={
    #             'type': 'text',
    #             'class': 'inputBox',
    #             'required': 'required',
    #             'id': 'name'
    #         }),
    #         'phone': TextInput(attrs={
    #             'type': 'tel',
    #             'class': 'inputBox',
    #             'required': 'required',
    #             'id': 'phone'
    #         }),
    #         'peopleAmount': NumberInput(attrs={
    #             'type': 'number',
    #             'class': 'inputBox',
    #             'required': 'required',
    #             'id': 'peopleAmount',
    #             'min': '5',
    #             'max': '20'
    #         })
    #     }
