from django.urls import path
from learning.views import HomeView
from django.contrib.auth.decorators import login_required

""" Templateview se utiliza para mostrar información estática, peticiones get """
urlpatterns = [
    path('profile/', login_required(HomeView.as_view()), name="profile"),
]

"""  path('home', views.home, name="home"), luego en el form utilizar  action="{% url 'home' %}"  """
