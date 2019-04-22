from rest_framework import serializers

from .models import Doc


class DocSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(read_only=True, view_name='docs:doc-detail')
    author = serializers.HyperlinkedRelatedField(read_only=True, view_name='accounts:account-detail')
    authors_shared = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='accounts:account-detail')

    class Meta:
        model = Doc
        fields = ('id', 'url', 'author', 'title', 'body', 'created_at', 'updated_at', 'authors_shared')
