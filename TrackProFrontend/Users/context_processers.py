import requests
from helpers.static_info import *



def getMenu(request):
    token = request.session.get('token')
    Menu = request.session.get('Menu')
    Firstname = request.session.get('Firstname')
    Lastname = request.session.get('Lastname')
    Designation = request.session.get('Designation')
    userID = request.session.get('userID')
    userEmployeeId=request.session.get('userEmployeeId')
    rules = request.session.get('rules')
    roleID = request.session.get('roleID')
    rolename = request.session.get('rolename')
    
    companylogo = request.session.get('companylogo')
    userphoto = request.session.get('userPhoto')
    is_staff = request.session.get('is_staff')
    
    taskmappingURL = remoteURL+'users/api/basegetMapping?userID={}'.format(userID)
    taskmappingresponse = requests.get(taskmappingURL)
    taskmappingdata = taskmappingresponse.json()


    managerurl = remoteURL+'users/api/taskmanagercheck?userID={}'.format(userID)
    managerresponse = requests.get(managerurl)
    bmanagerdata = managerresponse.json()
        

   
    return {'token':token,'Menulist':Menu,'Designation':Designation,
            'Firstname':Firstname,'rolename':rolename,
            'Lastname':Lastname,'userID':userID,
            'userEmployeeId':userEmployeeId,
            'rules':rules,'roleID':roleID,
            'ImageURL':ImageURL,'companylogo':companylogo,
            'photo':userphoto,'basemanagerlist':taskmappingdata['data'],
            'basecheck_taskmanager':bmanagerdata['IsTaskmanager'],
            'basecheck_leavemanager':bmanagerdata['Isleavemanager'],
            'basebackendUrl':remoteURL,
            'basefrontendUrl':frontendURL,
            }