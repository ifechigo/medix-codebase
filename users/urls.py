from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_page, name='login'),
    path('signup/', views.sign_up_page, name='signup'),
    path('pratitioner-signup/', views.pratitioner_sign_up_page, name='pratitioner-signup'),
    path('logout/', views.logout, name='logout'),

    path('medical-record/', views.user_medical_record, name='medical-record'),
    path('statistics/', views.statistical_details, name='statistics'),
    
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
    
]
