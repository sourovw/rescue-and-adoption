from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registrationPage, name='register'),
    path('create-profile/', views.createProfile, name='createProfile'),
    path('profiles/', views.showProfiles, name='showProfiles'),
    path('profiles/<int:profile_id>', views.profileDetails, name='profile'),
]
