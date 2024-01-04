from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('about', views.about_view, name='about'),
    path('terms_and_conditions', views.terms_conditions_view, name='terms_conditions'),
]