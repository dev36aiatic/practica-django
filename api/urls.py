from django.urls import path
from django.urls.conf import include
from rest_framework import routers

from api.views import AddBoardView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('boards/new/', login_required(AddBoardView.as_view()), name="add_board")
]
