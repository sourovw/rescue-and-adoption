from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Adoption(models.Model):
    animal_id = models.PositiveIntegerField()
    adopter_name = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    zip_code = models.CharField(max_length=10, blank=True)
    contact_no = models.CharField(max_length=11)
    adopter_photo = models.ImageField(upload_to='forms/adoption/')
    closed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Form ID: {self.id}'

    def save(self):
        super().save()
        img = Image.open(self.adopter_photo.path)
        if img.height > 900 or img.width > 900:
            output_size = (900, 900)
            img.thumbnail(output_size)
            img.save(self.adopter_photo.path)


class Rescue(models.Model):
    animal_type = models.CharField(max_length=30)
    rescuer_name = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    zip_code = models.CharField(max_length=10, blank=True)
    contact_no = models.CharField(max_length=11)
    animal_photo = models.ImageField(upload_to='forms/rescue/')
    closed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Form ID: {self.id}'

    def save(self):
        super().save()
        img = Image.open(self.animal_photo.path)
        if img.height > 900 or img.width > 900:
            output_size = (900, 900)
            img.thumbnail(output_size)
            img.save(self.animal_photo.path)
