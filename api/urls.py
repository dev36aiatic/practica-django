from django.urls import path
from api.views import AddBoardView, AddIdeaView, HomeView, BoardsView, BoardDetailView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('profile/', login_required(HomeView.as_view()), name="profile"),
    path('boards/', login_required(BoardsView.as_view()), name="boards"),
    path('boards/<int:pk>/', login_required(BoardDetailView.as_view()), name="boards_id"),
    path('boards/<int:pk>/idea/', login_required(AddIdeaView.as_view()), name="new_idea"),
    path('boards/new/', login_required(AddBoardView.as_view()), name="add_board")
]
