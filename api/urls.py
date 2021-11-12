from django.urls import path
from api.views import AddBoardView, HomeView, BoardsView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('profile/', login_required(HomeView.as_view()), name="profile"),
    path('boards/', login_required(BoardsView.as_view()), name="boards"),
    path('boards/new/', login_required(AddBoardView.as_view()), name="add_board")
]
