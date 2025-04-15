from django import forms

class CreateNewService(forms.Form):
    name = forms.CharField(max_length=40)
    description = forms.CharField(widget=forms.Textarea, label='Description')
    price_hour = forms.DecimalField(decimal_places=2, max_digits=5, min_value=0.00)
    field = forms.ChoiceField(required=True, choices=[])

    def __init__(self, *args, choices=None, **kwargs):
        super().__init__(*args, **kwargs)
        if choices:
            self.fields['field'].choices = choices if choices else [('', 'Select a field')]

        # adding placeholders to form fields
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Enter Service Name',
            'autocomplete': 'off',
            'class': 'form-control',
        })

        self.fields['description'].widget.attrs.update({
            'placeholder': 'Enter Description',
            'class': 'form-control',
        })

        self.fields['price_hour'].widget.attrs.update({
            'placeholder': 'Enter Price per Hour',
            'class': 'form-control',
        })

        self.fields['field'].widget.attrs.update({
            'class': 'form-control',
        })


class RequestServiceForm(forms.Form):
    address = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter service address'})
    )
    service_time = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'placeholder': 'Hours needed'})
    )
