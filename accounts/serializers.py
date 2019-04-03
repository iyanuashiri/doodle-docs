from djoser import serializers

from .models import Account


class AccountSerializer(serializers.UserSerializer):

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name')
        read_only_fields = ('id', 'email',)
