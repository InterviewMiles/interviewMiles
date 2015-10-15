from rest_framework import serializers
from users.models import *

class UserResponceSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserResponce  