"""
URL configuration for crudproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name="login_page"),
    path('create_user/', views.create_user, name="create_user"),
    path('sucess/', views.sucess_page, name="sucess_page"),
    path('user_page/', views.user_page, name="user_page"),
    path('user_page/deleting_user/', views.delete_user, name="deleting_users"),
    path('deleted_user/', views.deleted_user, name="deleted_user"),
    path('update_user/', views.update_user, name="update_user")
]
