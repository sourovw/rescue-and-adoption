from django.urls import path
from . import views

urlpatterns = [
    path('rescue-form/', views.rescueForm, name='rescueForm'),
    path('adoption-form/', views.adoptionForm, name='adoptionForm'),

    path('submitted-rescue-forms/', views.submittedRescueForm, name='submittedRescueForm'),
    path('submitted-adoption-forms/', views.submittedAdoptionForm, name='submittedAdoptionForm'),
    
    path('submitted-adoption-forms/<int:form_id>', views.adoptionFormDetails, name='adoptionFormDetails'),
    path('submitted-rescue-forms/<int:form_id>', views.rescueFormDetails, name='rescueFormDetails'),
]
