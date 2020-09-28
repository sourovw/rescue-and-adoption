from django import forms
from .models import Adoption
from .models import Rescue


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = ['animal_id', 'adopter_name', 'address', 'city', 'zip_code', 'contact_no', 'adopter_photo']


class RescueForm(forms.ModelForm):
    class Meta:
        model = Rescue
        fields = ['animal_type', 'rescuer_name', 'address', 'city', 'zip_code', 'contact_no', 'animal_photo']
