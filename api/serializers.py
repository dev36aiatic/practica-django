from rest_framework import serializers
from .models import Board, Ideas, User

""" class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'id_number',
                  'email', 'photo', 'created_at', 'updated_at']
 """
























                  
""" 
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['name',
                  'owner',
                  'status',
                  'created_at',
                  'updated_at']

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideas
        fields = ['name',
                  'owner',
                  'status',
                  'created_at',
                  'updated_at']
 """