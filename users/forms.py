from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
        exclude = ['user', ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MedicalRecordForm(ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'


