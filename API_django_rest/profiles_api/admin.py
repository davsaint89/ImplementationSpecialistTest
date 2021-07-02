from django.contrib import admin

# Register your models here.
from profiles_api import models

admin.site.register(models.UserProfile) # se le da acceso al admin al modelo que se creo en models.py


