from rest_framework import serializers
from users.models import CheckUser


class CheckUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CheckUser