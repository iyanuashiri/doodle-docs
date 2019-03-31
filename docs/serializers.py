from rest_framework import serializers

from .models import Doc


class DocSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Doc
        fields = ('id', 'url', 'title', 'body', 'created_at', 'updated_at')

