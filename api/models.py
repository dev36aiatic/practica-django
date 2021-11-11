from django.db import models
from django import forms

from django.contrib.auth.models import User
    
class Board(models.Model):
    
    PUBLIC = 'PU'
    PRIVATE = 'PR'
    BOARD_STATUS = [
        (PUBLIC, 'Publico'),
        (PRIVATE, 'Privado')
    ]
    name = models.CharField(max_length=36)
    owner = models.ForeignKey(User, on_delete=models.CASCADE , null= True)
    status = models.CharField(max_length=2, choices=BOARD_STATUS, default=PUBLIC)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.id } - { self.name } | { self.owner }"
    
class Ideas(models.Model):
    PUBLIC = 'PU'
    PRIVATE = 'PR'
    BOARD_STATUS = [
        (PUBLIC, 'Publico'),
        (PRIVATE, 'Privado')
    ]
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null= True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null= True)
    name = models.CharField(max_length=36)
    status = models.CharField(max_length=2, choices=BOARD_STATUS, default=PUBLIC)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.id } - { self.name } | { self.owner }"

