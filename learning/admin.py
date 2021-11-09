from django.contrib import admin

from learning.models import Board, Ideas, User

# Register your models here.
admin.site.register(Board)
admin.site.register(User)
admin.site.register(Ideas)
