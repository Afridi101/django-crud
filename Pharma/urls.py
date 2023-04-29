"""
URL configuration for Pharma project.

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
from Auth import views as auth
from Home import views as home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', auth.login, name="login"),
    path('loging', auth.loging, name="loging"),
    path('logout', auth.logout, name="logout"),
    path('home', home.Home.home, name="home"),
    path('signup', auth.signup, name="signup"),
    path('user', home.Home.user, name="user"),
    path('add-form', home.Home.add_form, name='add-form'),
    path('edit-form/<int:id>', home.Home.edit_form, name='edit-form'),
    path('add-user', home.Home.add_user, name='add-user'),
    path('edit-user', home.Home.edit_user, name='edit-user'),
    path('delete-user/<int:id>', home.Home.delete_user, name='delete-user')
]
