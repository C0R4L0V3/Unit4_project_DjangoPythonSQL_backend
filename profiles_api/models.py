from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateTimeField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True, default='This user has not added a bio.')
    profile_picture = models.ImageField(
        upload_to='profile_picture/',                          
        blank=True, 
        null=True,
        default='../media/profile_picture/profile_picutre_placeholder.jpg'
        )

    def __str__(self):
        return self.user.username