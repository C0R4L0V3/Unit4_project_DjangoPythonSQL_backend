from django.db import models

# Create your models here.
class TagSchema(models.Model):
    tag_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'{self.tag_name}'