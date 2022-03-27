from django.contrib import admin
from .models import location, category, Image

# Register your models here.

admin.site.register(Image)
admin.site.register(location)
admin.site.register(category)