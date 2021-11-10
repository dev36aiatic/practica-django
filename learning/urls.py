from django.urls import path
from django.urls.conf import include
from learning import views
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('profile/', views.home,  name="profile"),
    path('users/', include(router.urls) )
]

"""  path('home', views.home, name="home"), luego en el form utilizar  action="{% url 'home' %}"  """