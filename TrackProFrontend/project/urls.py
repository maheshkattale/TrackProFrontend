from django.contrib import admin
from django.urls import path, include, re_path
from . import views as v
# from django.conf.urls import url

urlpatterns = [
    path('', v.projectlist, name='projectlist'),
    path('updateproject', v.updateproject, name='updateproject'),
    path('addProjectTask', v.addProjectTask, name='addProjectTask'),
    path('delete_project/<int:id>', v.delete_project, name='delete_project'),
    path('baseprojectlist', v.baseprojectlist, name='baseprojectlist'),

    #updatetask
    path('updateProjectTask/<int:id>', v.updateProjectTask, name='updateProjectTask'),
    path('holdProjectTask/<int:id>', v.holdProjectTask, name='holdProjectTask'),
    path('resumeProjectTask/<int:id>', v.resumeProjectTask, name='resumeProjectTask'),
    path('projectreport', v.projectreport, name='projectreport'),
    path('getProjectDetail',v.getProjectDetail, name="getProjectDetail"),
    path('getProjecttotaltime',v.getProjecttotaltime, name="getProjecttotaltime"),

    path('getnewProjectDetail',v.getnewProjectDetail, name="getnewProjectDetail"),
    path('searchProjectDetail',v.searchProjectDetail, name="searchProjectDetail"),
    path('paginationprojectlist',v.paginationprojectlist, name="paginationprojectlist"),
    path('excelprojectreport',v.excelprojectreport, name="excelprojectreport"),

    #user dashboard
    path('userdashboardlisting',v.userdashboardlisting, name="userdashboardlisting"),
    path('projectstasks',v.projectstasks, name="projectstasks"),

]