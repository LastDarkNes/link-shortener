from rest_framework import serializers
from .models import Link


class GetLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['full_link']
        extra_kwargs = {'full_link': {'required': True}}
