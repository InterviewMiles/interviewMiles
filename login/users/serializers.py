from rest_framework import serializers
from users.models import CheckUser


class CheckUserSerializer(serializers.Serializer):
	class Meta:
		model = CheckUser
		fields = ('exists',)