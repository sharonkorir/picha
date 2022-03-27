from django.contrib import admin
from .models import Owner, location, category, Image

# Register your models here.
admin.site.register(Owner)
admin.site.register(Image)
admin.site.register(location)
admin.site.register(category)