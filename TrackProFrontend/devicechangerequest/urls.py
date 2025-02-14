from django.contrib import admin
from django.urls import path
from . import views as v
# from django.conf.urls import url
urlpatterns = [
    path('devicechangerequestlist', v.devicechangerequestlist, name='devicechangerequestlist'),
    path('approvedevicechangerequest', v.approvedevicechangerequest, name='approvedevicechangerequest'),
    path('rejectdevicechangerequest', v.rejectdevicechangerequest, name='rejectdevicechangerequest'),

]