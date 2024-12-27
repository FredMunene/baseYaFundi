from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.db import transaction
from django.core.exceptions import ValidationError

from .models import User, Company, Customer


class DateInput(forms.DateInput):
    input_type = 'date'


def validate_email(value):
    # In case the email already exists in an email input in a registration form, this function is fired
    if User.objects.filter(email=value).exists():
        raise ValidationError(
            value + " is already taken.")


class CustomerSignUpForm(UserCreationForm):
    pass


class CompanySignUpForm(UserCreationForm):
    #  add the field is_company that is not in the UserCreationForm
    is_company = forms.BooleanField(required=False, initial=True, widget = forms.HiddenInput())

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'is_company']

    def save(self, commit = ...):
        user = super().save(commit=False)

        user.is_company = self.cleaned_data['is_company']

        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['autocomplete'] = 'off'
