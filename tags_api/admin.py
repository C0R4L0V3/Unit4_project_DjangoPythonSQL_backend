from django.contrib import admin

# Register your models here.
from .models import TagSchema
admin.site.register(TagSchema)