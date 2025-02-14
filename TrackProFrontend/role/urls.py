from django.contrib import admin
from django.urls import path, include, re_path
from . import views as v
# from django.conf.urls import url
urlpatterns = [
    path('', v.rolelsit, name='rolelsit'),
    path('updateRole', v.updateRole, name='updateRole'),
    path('getpermission', v.getpermission, name='getpermission'),
    path('permission', v.permission, name='permission'),

    #add super user
    # path('adduser', v.addsuperuser, name='addsuperuser'),
    path('updateuser/<int:id>', v.updatesuperuser, name='updatesuperuser'),
    path('delete_role/<int:id>', v.delete_role, name='delete_role'),
    path('userlist', v.superuserlist, name='superuserlist'),
]