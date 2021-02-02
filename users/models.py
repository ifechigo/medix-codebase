from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Users(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    medical_number = models.IntegerField(null=False)
    email = models.EmailField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class MedicalRecord(models.Model):
    users = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
    age = models.IntegerField(null=False)
    ethnicity = models.CharField(max_length=200, null=True)
    marital_status = models.CharField(max_length=200, null=True)
    employment_status = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    food_allergy = models.BooleanField(default=False, null=False)
    drug_allergy = models.BooleanField(default=False, null=False)
    emergency_medication = models.BooleanField(default=False, null=False)
    tetanus_injection = models.BooleanField(default=False, null=False)
    malaria = models.BooleanField(default=False, null=False)
    fever = models.BooleanField(default=False, null=False)
    disabilities = models.BooleanField(default=False, null=False)
    covid19 = models.BooleanField(default=False, null=False)
    ebola = models.BooleanField(default=False, null=False)
    ulcer = models.BooleanField(default=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.users.name

