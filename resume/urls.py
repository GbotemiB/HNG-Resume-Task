from django.contrib import admin
from django.urls.resolvers import URLPattern
from django.urls import path, include
from resume import views

urlpatterns = [
    path('', views.home, name='home'),
    path('formpage/', views.form_name_view, name='form_name')
]