from django.urls import path
from api.views import AddBoardView, AddIdeaView, BoardList, DeleteIdeaView, EditIdeaView, HomeView, BoardsView, BoardDetailView, UserList
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/', login_required(HomeView.as_view()), name="profile"),
    path('boards/', login_required(BoardsView.as_view()), name="boards"),
    path('boards/<int:pk>/', login_required(BoardDetailView.as_view()), name="boards_id"),
    path('boards/<int:pk>/idea/', login_required(AddIdeaView.as_view()), name="create_idea"),
    path('boards/<int:pk2>/idea/<int:pk>/', login_required(EditIdeaView.as_view()), name="update_idea"),
    path('boards/<int:pk2>/idea/<int:pk>/delete/', login_required(DeleteIdeaView.as_view()), name="delete_idea"),
    path('boards/new/', login_required(AddBoardView.as_view()), name="add_board"),
    path('users/', UserList.as_view(), name="users"),
    path('boards_api/', BoardList.as_view(), name="boards_api")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
