from djoser import serializers
from rest_framework import serializers as serialize

from .models import Account


class AccountSerializer(serializers.UserSerializer):
    docs = serialize.HyperlinkedRelatedField(read_only=True, many=True, view_name='docs:doc-detail')
    url = serialize.HyperlinkedRelatedField(read_only=True, view_name='accounts:account-detail')
    docs_shared = serialize.HyperlinkedRelatedField(read_only=True, many=True, view_name='docs:doc-detail')

    class Meta:
        model = Account
        fields = ('id', 'url', 'email', 'first_name', 'last_name', 'docs', 'docs_shared')
        read_only_fields = ('id', 'email',)
