from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    full_name = models.CharField(max_length=60)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    zip_code = models.CharField(max_length=10)
    contact_no = models.CharField(max_length=11)
    profile_picture = models.ImageField(upload_to='users/pictures')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.full_name}\'s Profile'

    def save(self):
        super().save()
        img = Image.open(self.profile_picture.path)
        if img.height > 900 or img.width > 900:
            output_size = (900, 900)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)
