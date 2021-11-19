from django.db.models import fields
from rest_framework import serializers
from api.models import Board, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name',
                  'last_name', 'id_num', 'profile_picture')

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields=  ('id', 'name', 'owner', 'status')