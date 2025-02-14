from django.contrib import admin
from django.urls import path, include, re_path
from . import views as v
# from django.conf.urls import url
urlpatterns = [
    path('getUserWeek', v.getUserWeek, name='getUserWeek'),
   

    path('getlastTask', v.getlastTask, name='getlastTask'),
    path('getAllTask', v.getAllTask, name='getAllTask'),
    path('getAssignTask', v.getAssignTask, name='getAssignTask'),
    path('getTaskTrackProScore', v.getTaskTrackProScore, name='getTaskTrackProScore'),
    path('mytrackproscore', v.mytrackproscore, name='mytrackproscore'),
    path('addParticualrIntermediateTrackProResult', v.addParticualrIntermediateTrackProResult, name='addParticualrIntermediateTrackProResult'),
    path('trackpro-rank', v.trackpro_rank, name='trackpro_rank'),
    path('trackpro-result', v.trackproresult, name='trackproresult'),

    #new deptwise rank page
    path('dept-trackpro-result', v.depttrackproresult, name='depttrackproresult'),
    path('gettableinfo', v.gettableinfo, name='gettableinfo'),
    path('getweeklyempinfo', v.getweeklyempinfo, name='getweeklyempinfo'),
    path('getavgempinfo', v.getavgempinfo, name='getavgempinfo'),
    path('viewweeklyempinfo', v.viewweeklyempinfo, name='viewweeklyempinfo'),
    path('publishdeptwiserank', v.publishdeptwiserank, name='publishdeptwiserank'),

    path('trackproResultWeek', v.trackproResultWeek, name='trackproResultWeek'),
    path('publishrank', v.publishrank, name='publishrank'),
    path('getmanagerWeek', v.getmanagerWeek, name='getmanagerWeek'),
    path('Getemployeerankinformation', v.Getemployeerankinformation, name='Getemployeerankinformation'),
    path('trackprocheckreport', v.trackprocheckreport, name='trackprocheckreport'),
    path('trackprocheckreportdata', v.trackprocheckreportdata, name='trackprocheckreportdata'),
    path('reportfinalsubmit', v.reportfinalsubmit, name='reportfinalsubmit'),
    path('getassignbytaskdata', v.getassignbytaskdata, name='getassignbytaskdata'),
    path('updatetaskassignby', v.updatetaskassignby, name='updatetaskassignby'),
    
    
]