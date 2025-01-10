from django.contrib import admin

# Register your models here.
from .models import BlogPostSchema
admin.site.register(BlogPostSchema)