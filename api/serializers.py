from django.db.models import fields
from rest_framework import serializers
from api.models import Board, Ideas, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name',
                  'last_name', 'id_num', 'profile_picture')


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'name', 'owner', 'status')


class IdeasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideas
        fields = ('id', 'name', 'owner', 'board', 'status')


class CreateIdeasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideas
        fields = ('id', 'name', 'owner', 'board', 'status')


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name', 'id_num', 'profile_picture']
