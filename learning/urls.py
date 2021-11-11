from django.urls import path
from learning.views import HomeView

""" Templateview se utiliza para mostrar información estática, peticiones get """
urlpatterns = [
    path('profile/', HomeView.as_view(), name="profile"),
]

"""  path('home', views.home, name="home"), luego en el form utilizar  action="{% url 'home' %}"  """
