from django.urls import path
from . import views

#path syntax -> url,view,name
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about_view, name='about'),
    path('terms_and_conditions', views.terms_conditions_view, name='terms_conditions'),
]