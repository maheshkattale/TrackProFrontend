from django.contrib import admin
from django.urls import path, include, re_path
from . import views as v
# from django.conf.urls import url
urlpatterns = [
    path('', v.usertasklist, name='usertasklist'),
    path('userdashboard', v.userdashboard, name='userdashboard'),
    path('get_project_list', v.get_project_list, name='get_project_list'),
    path('ThreeParamData', v.ThreeParamData, name='ThreeParamData'),
    path('activeusersHome', v.activeUsers_dashboard, name='activeUsers_dashboard'),
    path('record', v.employee_record , name='employee_record'),
    path('addTaskAjax', v.addTaskAjax, name='addTaskAjax'),
    path('get_taskdetail', v.get_taskdetail, name='get_taskdetail'),
    path('updateParticularTaskZone', v.updateParticularTaskZone, name='updateParticularTaskZone'),
    path('Add_duplicateTask',v.Add_duplicateTask,name='Add_duplicateTask'),
    path('Add_Continuetask',v.Add_Continuetask,name='Add_Continuetask'),
    path('usercurrentweektask', v.usercurrentweektask, name='usercurrentweektask'),
    
    path('updateTaskZoneMultiple', v.updateTaskZoneMultiple, name='updateTaskZoneMultiple'),
    path('updatezone_Tasklist', v.updatezone_Tasklist, name='updatezone_Tasklist'),

    path('coordinator', v.taskcoordinator, name='taskcoordinator'),
    path('employee_task/<int:id>', v.employee_task, name='employee_task'),
    path('report', v.taskTrackProcoordinator, name='taskTrackProcoordinator'),
    path('getyearlist', v.getyearlist, name='getyearlist'),
    path('getweeklist', v.getweeklist, name='getweeklist'),
    path('getemployeelist', v.getemployeelist, name='getemployeelist'),
    path('getsupervisorlist', v.getsupervisorlist, name='getsupervisorlist'),
    
    
    
    #added
    path('deleteTask/<int:id>', v.deleteTask, name="deleteTask"),
    
    path('getTaskInfo/<int:id>', v.getTaskInfo, name="getTaskInfo"),
    path('updateTaskAjax/<int:id>', v.updateTaskAjax, name='updateTaskAjax'),

    # path('manageremployeelist', v.manageremployeelist, name='manageremployeelist'),
    path('manageremptask', v.manageremptask, name='manageremptask'),
    path('empcurrentweektask', v.empcurrentweektask, name='empcurrentweektask'),
    path('checktaskbymanagerUI/<int:id>', v.checktaskbymanagerUI, name='checktaskbymanagerUI'),
    path('addTaskbymanager', v.addTaskbymanager, name='addTaskbymanager'),
    path('Zonestatusbymanager', v.Zonestatusbymanager, name='Zonestatusbymanager'),
    path('taskbonusbymanager', v.taskbonusbymanager, name='taskbonusbymanager'),
    

    path('Employeetaskinfom',v.Employeetaskinfom, name='Employeetaskinfom'),
    path('Managertaskinfom',v.Managertaskinfom, name='Managertaskinfom'),
    path('ManagerReview',v.ManagerReview,name='ManagerReview'),
    path('listmanagerreview',v.listmanagerreview,name='listmanagerreview'),

    path('ReviewEmployeelist',v.ReviewEmployeelist,name='ReviewEmployeelist'),
    path('ReviewEmployeetasklist',v.ReviewEmployeetasklist,name='ReviewEmployeetasklist'),
    path('finalsubmitall',v.finalsubmitall,name='finalsubmitall'),
    
    #weeklyreport
    path('Weeklyreport',v.Weeklyreport,name='Weeklyreport'),
    path('weeklyreportdata',v.weeklyreportdata,name='weeklyreportdata'),
    path('weeklyprojectreportdata',v.weeklyprojectreportdata,name='weeklyprojectreportdata'),
    path('previoustasktime',v.previoustasktime,name='previoustasktime'),
    path('weekdates',v.weekdates,name='weekdates'),
    
    path('EMPWeeklyreport',v.EMPWeeklyreport,name='EMPWeeklyreport'),
    path('EMPWeeklydata',v.EMPWeeklydata,name='EMPWeeklydata'),

    #remarks
    path('addmanagertaskremark',v.addmanagertaskremark,name='addmanagertaskremark'),
    path('addemployertaskremark',v.addemployertaskremark,name='addemployertaskremark'),
    path('taskremarklist',v.taskremarklist,name='taskremarklist'),
    path('dashboardtaskremarklist',v.dashboardtaskremarklist,name='dashboardtaskremarklist'),

    
    path('getweeklytask',v.getweeklytask,name='getweeklytask'),
    path('search_tasks',v.search_tasks,name='search_tasks'),

]