from django.contrib import admin
from django.urls import path, include, re_path
from . import views as v
# from django.conf.urls import url
urlpatterns = [
    path('', v.applyleave, name='applyleave'),
    path('apply_leave_front', v.apply_leave_front, name='apply_leave_front'),

    path('leavemapping', v.leavemapping, name='leavemapping'), 
    path('get_leavemapping_employee_list', v.get_leavemapping_employee_list, name='get_leavemapping_employee_list'),   
    path('request', v.leaverequest, name='leaverequest'),    
    path('statustypeleaveajax/<int:id>', v.statustypeleaveajax, name='statustypeleaveajax'),    
    path('statustypeleave/<int:id>', v.statustypeleave, name='statustypeleave'),    
    path('deleteleave/<int:id>', v.deleteleave, name='deleteleave'),    
    path('updateleave/<int:id>', v.updateleave, name='updateleave'),    
    path('updateapplyleave/<int:id>', v.updateapplyleave, name='updateapplyleave'),    
    path('updateleavemapping', v.updateleavemapping, name='updateleavemapping'),
    path('leavemappingOnchangeAjax', v.leavemappingOnchangeAjax, name='leavemappingOnchangeAjax'),
    path('attendance', v.attendance, name='attendance'),
    path('reject_approved_application', v.reject_approved_application, name='reject_approved_application'),
    path('approve_rejected_application', v.approve_rejected_application, name='approve_rejected_application'),
    path('leaveactionFront', v.leaveactionFront, name='leaveactionFront'),
    path('FilterleaveListAPIfront', v.FilterleaveListAPIfront, name='FilterleaveListAPIfront'),
    path('get_filter_leaves', v.get_filter_leaves, name='get_filter_leaves'),
    path('Apply_Leave_Mapping', v.Apply_Leave_MappingFront, name='Apply_Leave_MappingFront'),
    path('leave_mapping_emp_filter', v.leave_mapping_emp_filter, name='leave_mapping_emp_filter'),
    path('get_per_date_leaves_count', v.get_per_date_leaves_count, name='get_per_date_leaves_count'),

    path('widhrawapplication', v.widhrawapplication, name='widhrawapplication'),
    path('past_leaves', v.past_leaves, name='past_leaves'),

    path('leavedetails/<str:leaveid>/<str:manager_approvel_id>', v.leavedetails, name='leavedetails'),
    path('get_leavemapping_employee_list', v.get_leavemapping_employee_list, name='get_leavemapping_employee_list'),
    path('compoff_granted', v.compoff_granted, name='compoff_granted'), 

    path('leavetype', v.leavetype, name='leavetype'), 
    path('delete_leavetype', v.delete_leavetype, name='delete_leavetype'), 
    path('update_leavetype', v.update_leavetype, name='update_leavetype'), 
    path('add_leavetype', v.add_leavetype, name='add_leavetype'), 












]