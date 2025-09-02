from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(forms.Form):
    email = forms.EmailField(
        label='Enter email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}
        )
    )
    username = forms.CharField(
        label='Enter login',
        required=True,
        help_text='You cannot enter symbols: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter login'}
                               )
    )
    some = forms.ModelChoiceField(queryset=User.objects.all())
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
        fields = ['username', 'email', 'some']