from django.contrib import admin
from django.urls import path, include, re_path
from . import views as v
# from django.conf.urls import url
urlpatterns = [
    path('shift_swap_requests', v.shift_swap_requests, name='shift_swap_requests'),
    path('get_shift_swap_applications', v.get_shift_swap_applications, name='get_shift_swap_applications'),
    path('reject_application', v.reject_application, name='reject_application'),
    path('approve_application', v.approve_application, name='approve_application'),
]