"""practicas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from learning import views
from allauth.account import views as allauth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', allauth_views.login, name="account_login"),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('learning.urls')),
]
""" <a href="{% url 'account_login' %}">Login</a> """

"""  path('home', views.home, name="home"), luego en el form utilizar  action="{% url 'home' %}"  """
"""  url(r"^signup/$", allauth_views.signup, name="account_signup"),
    url(r"^login/$", allauth_views.login, name="account_login"),
    url(r"^logout/$", allauth_views.logout, name="account_logout"), """