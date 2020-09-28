from django.contrib import admin
from .models import Adoption
from .models import Rescue


admin.site.register(Adoption)
admin.site.register(Rescue)
