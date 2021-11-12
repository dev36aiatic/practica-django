from django.contrib import admin

from api.models import Board, Ideas, User

# Register your models here.
admin.site.register(Board)
admin.site.register(Ideas)
admin.site.register(User)
