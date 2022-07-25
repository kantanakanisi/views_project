from django import forms
from django.contrib.auth.models import User
from user.models import Profile
import logging

application_logger = logging.getLogger('application-logger')

class UserForm(forms.ModelForm):
    username = forms.CharField(label='username')
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    website = forms.URLField(label='url')

    class Meta:
        model = Profile
        fields = ('website',)

class LoginForm(forms.Form):
    application_logger.debug('login')
    username = forms.CharField(label='username', max_length=150)
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password !=confirm_password:
            raise forms.ValidationError('password error')
