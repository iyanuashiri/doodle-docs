from rest_framework import serializers

from .models import Doc


class DocSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(read_only=True, view_name='doc-detail')
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Doc
        fields = ('id', 'url', 'author', 'title', 'body', 'created_at', 'updated_at', 'authors_shared')
