"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings

from django.views.static import serve
from django.conf.urls.static import static
from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from backend import settings
router = routers.DefaultRouter(trailing_slash=False)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', obtain_auth_token, name='token'),
    path('', include(router.urls)),
    path('users-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/user/', include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls'))
]
