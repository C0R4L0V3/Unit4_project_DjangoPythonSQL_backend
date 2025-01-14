from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1

    #  method to generate teh media url
    def get_profile_picture(self, obj):
        #check if profile picture is set
        if obj.profile_picture and hasattr(obj.profile_picture, 'url'):
            return f"{settings.MEDIA_URL}{obj.profile_picture}"
        #Return defual placeholder in no profile picture exsists
        return f"{settings.MEDIA_URL}profile_picture/profile_picture_placeholder.jpg"