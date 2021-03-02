from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        min_length=4,
        max_length=50,
        label='Ваше имя',
    )

    last_name = forms.CharField(
        min_length=4,
        max_length=50,
        label='Ваша фамилия'
    )

    email = forms.EmailField(
        min_length=10,
        max_length=50,
        widget=forms.EmailInput(),
        label='Email'
    )

class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(
    required=False, 
    label="password",
    max_length=32, 
    strip=False,
    widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'last_name', 'first_name' ,'email']


    
