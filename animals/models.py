from django.db import models
from PIL import Image


class Animal(models.Model):
    category = models.CharField(max_length=30)
    gender = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='animals/photos/')
    adopted = models.BooleanField(default=False)

    def __str__(self):
        return f'ID : {self.id} - {self.category}'

    def save(self):
        super().save()
        img = Image.open(self.picture.path)
        if img.height > 900 or img.width > 90:
            output_size = (900, 900)
            img.thumbnail(output_size)
            img.save(self.picture.path)
