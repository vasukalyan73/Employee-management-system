from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Employee


class EmployeeForm(forms.ModelForm):
    """Form for creating and updating employee records"""
    
    class Meta:
        model = Employee
        fields = ['emp_name', 'emp_role', 'emp_loc', 'emp_ph_no']
        widgets = {
            'emp_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Employee Name',
                'required': True
            }),
            'emp_role': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Employee Role',
                'required': True
            }),
            'emp_loc': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Employee Location',
                'required': True
            }),
            'emp_ph_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Phone Number',
                'type': 'tel',
                'required': True
            }),
        }
        labels = {
            'emp_name': 'Employee Name',
            'emp_role': 'Employee Role',
            'emp_loc': 'Employee Location',
            'emp_ph_no': 'Phone Number',
        }


class RegistrationForm(UserCreationForm):
    """Form for user registration"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a username'
        })
    )
    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First name (optional)'
        })
    )
    last_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last name (optional)'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email


class LoginForm(forms.Form):
    """Form for user login"""
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )
