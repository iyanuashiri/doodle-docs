from rest_framework import serializers

from .models import Doc


class DocSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Doc
        fields = ('id', 'url', 'title', 'body', 'created_at', 'updated_at')

