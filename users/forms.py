from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.db import transaction
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db import IntegrityError
import uuid

from .models import User, Company, Customer


class DateInput(forms.DateInput):
    input_type = 'date'


def validate_email(value):
    # In case the email already exists in an email input in a registration form, this function is fired
    if User.objects.filter(email=value).exists():
        raise ValidationError(
            value + " is already taken.")

class CustomerSignUpForm(UserCreationForm):
    
    is_customer = forms.BooleanField(required=False, initial=True, widget=forms.HiddenInput())
    first_name = forms.CharField(max_length=150, required=True, label="First Name")
    last_name = forms.CharField(max_length=150, required=True, label="Last Name")
    birth = forms.DateField(required=True, label="Date of Birth")
        
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'is_customer']

    def save(self, commit=True):
        # Get the user object from the form
        user = super().save(commit=False)

        # Set custom fields
        user.is_customer = self.cleaned_data['is_customer']
        user.is_company = False  # Explicitly mark as not a company
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        # Generate a unique username based on the first name and UUID
        if not user.username:
            user.username = slugify(self.cleaned_data['first_name'])

        # Save the user object and related data (if commit=True)
        if commit:
            user.save()

        return user

    

class CompanySignUpForm(UserCreationForm):
    #  add the field is_company that is not in the UserCreationForm
    is_company = forms.BooleanField(required=False, initial=True, widget = forms.HiddenInput())
    field = forms.ChoiceField(choices=Company._meta.get_field('field').choices, label="Field of Work")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'is_company']

    def save(self, commit = True):
        user = super().save(commit=False)
        user.is_company = self.cleaned_data['is_company']
        useris_customer = False
        #  Generate a unique username based on the email

        if not user.username:
            user.username = slugify(self.cleaned_data['email'])

        if commit:
            try:
                user.save()
                # Create a related Company instance
                Company.objects.create(user=user, field=self.cleaned_data['field'])

            except IntegrityError:
                raise ValidationError("a user with this username already exists")
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['autocomplete'] = 'off'

