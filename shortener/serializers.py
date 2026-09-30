from rest_framework import serializers
from .models import ShortURL

class ShortURLSerializer(serializers.ModelSerializer):
    # Mapping our Python snake_case to the required JSON camelCase
    shortCode = serializers.CharField(source='short_code', read_only=True)
    createdAt = serializers.DateTimeField(source='created_at', read_only=True)
    updatedAt = serializers.DateTimeField(source='updated_at', read_only=True)
    accessCount = serializers.IntegerField(source='access_count', read_only=True)

    class Meta:
        model = ShortURL
        fields = ['id', 'url', 'shortCode', 'createdAt', 'updatedAt', 'accessCount']