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


# Create your views here.


def home(request):
    return render(request, 'base.html')


def pratitioner_sign_up_page(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='doctor')

            user.groups.add(group)

            messages.success(request, 'Account created for ' + username)
            return redirect('login')

    
    context = { 'form': form}
    return render(request, 'users/register.html', context)


def sign_up_page(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            username = form.cleaned_data.get('username')

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
    return redirect('home')


@login_required(login_url='login')
def user_medical_record(request):

    #MedicalFormSet = inlineformset_factory(Users, MedicalRecord, fields=('__all__'))

    #user = request.get(user)

    form = MedicalRecordForm()

    if request.method == 'POST':

        form = MedicalRecordForm(request.POST)

        if form.is_valid():
            # report = form.save(commit=False)
            form.save()
            return HttpResponse('thanks')
        # else:
        #     form = MedicalForm()

        # form = CreateUserForm()


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


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()

def statistical_details(request):


    context = {}
    return render(request, '', context)