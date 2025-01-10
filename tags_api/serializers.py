from rest_framework import serializers
from .models import TagSchema

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagSchema
        fields = '__all__'