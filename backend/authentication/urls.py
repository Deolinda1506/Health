from django.urls import path
from . import views
from authentication import views as auth_views

urlpatterns = [
    # Activation and Registration
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('api/register', views.register, name='register'),

    # Health Metrics Management
    path('api/get_health_metrics', views.get_health_metrics, name='get_health_metrics'),
    path('api/update_health_metrics', views.update_health_metrics, name='update_health_metrics'),

    # Availability and Profile
    path('api/change_availability', views.change_availability, name='change_availability'),
    path('api/get_profile', views.get_profile, name='get_profile'),
    path('', auth_views.home, name='home'),  # This will route the root URL to the home view

]