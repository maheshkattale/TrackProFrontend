from django.contrib import admin
from django.urls import path, include, re_path
from . import views as v
# from django.conf.urls import url
urlpatterns = [

    path('packetlist', v.packetlist, name='packetlist'),
    path('update_packet', v.update_packet, name='update_packet'),
    path('delete_packet', v.delete_packet, name='delete_packet'),



    path('packetmapping', v.packetmapping, name='packetmapping'),
    path('get_packet_mapped_employees', v.get_packet_mapped_employees, name='get_packet_mapped_employees'),
    path('apply_employees_packet_mapping', v.apply_employees_packet_mapping, name='apply_employees_packet_mapping'),
    path('packetrulebuilder', v.packetrulebuilder, name='packetrulebuilder'),


    path('apply_packet_rules', v.apply_packet_rules, name='apply_packet_rules'),
    path('get_packet_leave_rules', v.get_packet_leave_rules, name='get_packet_leave_rules'),


]