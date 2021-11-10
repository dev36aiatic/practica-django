from django.urls import path
from learning import views

urlpatterns = [
    path('profile/', views.home,  name="profile"),
]

"""  path('home', views.home, name="home"), luego en el form utilizar  action="{% url 'home' %}"  """