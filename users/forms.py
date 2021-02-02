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


class RecordForm(forms.Form):
    age = forms.IntegerField()
    ethnicity = forms.CharField(max_length=200)
    marital_status = forms.CharField(max_length=200)
    employment_status = forms.CharField(max_length=200)
    gender = forms.CharField(max_length=50)
    food_allergy = forms.BooleanField()
    drug_allergy = forms.BooleanField()
    emergency_medication = forms.BooleanField()
    tetanus_injection = forms.BooleanField()
    malaria = forms.BooleanField()
    fever = forms.BooleanField()
    disabilities = forms.BooleanField()
    covid19 = forms.BooleanField()
    ebola = forms.BooleanField()
    ulcer = forms.BooleanField()
