from django.urls import path
from api.views import AboutView, AddBoardView, AddIdeaView, AddReplyView, AllContactsView, BoardList, ContactView, CreateIdeas, CreateUser, DeleteContactView, DeleteIdeaView, DeleteSingleUserView, EditContactView, EditIdeaView, BoardsView, BoardDetailView, HomeView, IdeasList, ProfileView, ServicesView, SingleUserView, UserList
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', login_required(HomeView.as_view()), name="home"),
    path('profile/', login_required(ProfileView.as_view()), name="profile"),
    path('about/', login_required(AboutView.as_view()), name="about"),
    path('services/', login_required(ServicesView.as_view()), name="services"),
    path('contact/', login_required(ContactView.as_view()), name="contact"),
    path('contacts/', login_required(AllContactsView.as_view()), name="all_contacts"),
    path('contacts/<int:pk>/', login_required(AddReplyView.as_view()), name="reply_to_contact"),
    path('contacts/<int:pk>/delete/', login_required(DeleteContactView.as_view()), name="delete_contact"),
    path('contacts/<int:pk>/edit/', login_required(EditContactView.as_view()), name="edit_contact"),
    path('boards/', login_required(BoardsView.as_view()), name="boards"),
    path('boards/<int:pk>/', login_required(BoardDetailView.as_view()), name="boards_id"),
    path('boards/<int:pk>/idea/', login_required(AddIdeaView.as_view()), name="create_idea"),
    path('boards/<int:pk2>/idea/<int:pk>/', login_required(EditIdeaView.as_view()), name="update_idea"),
    path('boards/<int:pk2>/idea/<int:pk>/delete/', login_required(DeleteIdeaView.as_view()), name="delete_idea"),
    path('boards/new/', login_required(AddBoardView.as_view()), name="add_board"),
    path('users/', UserList.as_view(), name="users"),
    path('boards_api/', BoardList.as_view(), name="boards_api"),
    path('ideas/', IdeasList.as_view(), name="ideas"),
    path('create_idea/', CreateIdeas.as_view(), name="create_ideas"),
    path('create/', CreateUser.as_view(), name="create"),
    path('list/', UserList.as_view(), name="users_list"),
    path('user/<int:pk>/', SingleUserView.as_view(), name="single_user"),
    path('delete/<int:pk>/', DeleteSingleUserView.as_view(), name="delete_single_user"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
