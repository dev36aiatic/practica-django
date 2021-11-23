from django.contrib import admin

from api.models import Board, Contact, Ideas, ReplyMessage, User

# Register your models here.
admin.site.register(Board)
admin.site.register(Ideas)
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(ReplyMessage)
