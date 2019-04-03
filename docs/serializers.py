from rest_framework import serializers

from .models import Doc


class DocSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Doc
        fields = ('id', 'url', 'author', 'title', 'body', 'created_at', 'updated_at', 'authors_shared')
