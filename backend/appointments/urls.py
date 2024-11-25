from django.urls import path
from . import views


urlpatterns = [
    # Matching Endpoints
    path('get_random_match', views.random_match, name="get_random"),
    
    # Doctor Management
    path('get_available_doctors', views.get_available_doctors, name="get_available_doctors"),
    path('get_all_doctors', views.get_all_doctors, name="get_all_doctors"),
    path('get_appointments/<int:doctor_id>/', views.get_doctor_appointments, name="get_doctor_appointments"),
    
    # Appointment Management
    path('get_upcoming_appointments', views.get_upcoming_appointments, name="get_upcoming_appointments"),
    path('get_past_appointments', views.get_past_appointments, name="get_past_appointments"),
    path('create_appointment', views.create_appointment, name="create_appointment"),
    path('<int:id>/cancel', views.cancel_appointment, name="cancel_appointment"),
    path('update_appointment', views.update_appointment, name="update_appointment"),
    path('get_all_past_appointments', views.get_all_past_appointments, name="get_all_past_appointments"),
    path('get_all_future_appointments', views.get_all_future_appointments, name="get_all_future_appointments"),
    
    # Call Management
    path('join_call', views.join_call, name="join_call"),
    
    # Prescription Management
    path('create_prescription', views.create_prescription, name="create_prescription"),
    path('<id>/<token>/invalidate/', views.invalidate_prescription, name="invalidate_prescription"),
    path('ask_for_refill', views.ask_for_refill, name="ask_for_refill"),
    path('grant_refill', views.grant_refill, name="grant_refill"),
    
    # Report Management
    path('create_report', views.create_report, name="create_report"),
    path('home/', views.homepage, name='appointments-home'),

]
