from django import forms
from django.forms import fields
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = fields.CharField(max_length=18,
                                min_length=6,
                                required=True,
                                error_messages={
                                    'required':'The Username is required,please try input it agian',
                                    'min_length':'Username must be between 8 and 16 characters long',
                                    'max_length':'Username must be between 8 and 16 characters long'
                                })
    password = fields.CharField(max_length=18,
                                min_length=6,
                                required=True,
                                widget=forms.PasswordInput,
                                error_messages={
                                    'required': 'The Passwords is required,please try input it agian',
                                    'min_length': 'Passwords must be between 8 and 16 characters long',
                                    'max_length': 'Passwords must be between 8 and 16 characters long'
                                })

class RegisterForm(forms.Form):

    username = fields.CharField(max_length=18,
                                min_length=6,
                                required=True
                                )
    password = fields.CharField(max_length=18,
                                min_length=6,
                                widget=forms.PasswordInput,
                                required=True,
                                )
    class Meta:
        model = User
        fields = ('username','password',)