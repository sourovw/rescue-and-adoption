from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.showAnimals, name='showAnimals'),
    path('animals/<int:animal_id>', views.animalDetails, name='animalDetails'),
]
