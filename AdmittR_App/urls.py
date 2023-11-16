from django.urls import path
from . import views

urlpatterns = [
    path('admission-form/', views.admission_form, name='admission_form'),
]
