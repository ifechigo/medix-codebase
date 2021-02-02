from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.forms import inlineformset_factory
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

from .models import *
from .forms import *
from .filters import *
from .decorators import *


# Create your views here.


def home(request):
    return render(request, 'base.html')


def pratitioner_sign_up_page(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='doctor')

            user = form.save(commit=False)

            user.save()

            user.groups.add(group)

            user.save()

            messages.success(request, 'Account created for ' + username)
            return redirect('login')

    
    context = { 'form': form}
    return render(request, 'users/register.html', context)


def sign_up_page(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='patient')

            user = form.save(commit=False)

            user.save()

            user.groups.add(group)

            user.save()

            messages.success(request, 'Account created for ' + username)
            return redirect('login')
    
    context = { 'form': form}
    return render(request, 'users/register.html', context)


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'users/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['patient'])
def user_medical_record(request):

    form = MedicalRecordForm()

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)

        if form.is_valid():
            age = form.cleaned_data['age']
            ethnicity = form.cleaned_data['ethnicity']
            marital_status = form.cleaned_data.get('marital_status')
            employment_status = form.cleaned_data.get('employment_status')
            gender = form.cleaned_data.get('gender')
            food_allergy = form.cleaned_data.get('food_allergy')
            drug_allergy = form.cleaned_data.get('drug_allergy')
            emergency_medication = form.cleaned_data.get('emergency_medication')
            tetanus_injection = form.cleaned_data.get('tetanus_injection')
            malaria = form.cleaned_data.get('malaria')
            fever = form.cleaned_data.get('fever')
            disabilities = form.cleaned_data.get('disabilities')
            covid19 = form.cleaned_data.get('covid19')
            ebola = form.cleaned_data.get('ebola')
            ulcer = form.cleaned_data.get('ulcer')

            medical_record = form.save(commit=False)

            medical_record.save()
            return HttpResponseRedirect('thanks')

    else:
        form = RecordForm()
        
    context = { 'form': form }
    return render(request, 'users/record.html', context)


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='users/chart.html')
line_chart_json = LineChartJSONView.as_view()

def statistical_details(request):


    context = {}
    return render(request, '', context)