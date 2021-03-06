from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label="Повторение пароля",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = None
        self.fields['username'].widget.attrs['id'] = 'register-form-input-username'
        self.fields['password1'].widget.attrs['id'] = 'register-form-input-password1'
        self.fields['password2'].widget.attrs['id'] = 'register-form-input-password2'
