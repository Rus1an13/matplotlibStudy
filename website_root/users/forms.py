from django import forms
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}
        )
    )
    # phone = forms.CharField(
    #     label='Введите номер телефона',
    #     required=True,
    #     widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}
    #     )
    # )    
    username = forms.CharField(
        label='Имя',
        required=True,
        help_text='You cannot enter symbols: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter login'}
                               )
    )
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(
        label='Enter password',
        required=True,
        help_text='The password should not be small and simple',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
    )
    password2 = forms.CharField(
        label='Confirm password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']