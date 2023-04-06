from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'image',
            'phone',
            'user_type',
            'gender',
            'password1',
            'password2',
            'birth_date',
        ]

class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username',
            'image',
            'email',
            'user_type',
            'phone',
            'gender',
            'birth_date',
        ]