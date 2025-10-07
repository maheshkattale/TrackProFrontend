from django.shortcuts import render
from helpers.static_info import *
from django.shortcuts import render,  HttpResponse, redirect
import requests
import json
import datetime
from Users.views import getfullname,tokenmsg,dashboardURL
from django.views.decorators.csrf import csrf_exempt
from Users.views import accessToPage,accessDenied,checksession
from django.contrib import messages
# Create your views here.



def createclient(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        # access = accessToPage(Menu, url)
        # if access == False:
        #     return redirect('users:accessDenied')
        data={}
        if request.method == 'POST' and 'add_form' in request.POST:
            data['ClientId'] = request.POST.get('createclient')
            data['Team'] = request.POST.getlist('Team')
            data['Client_ManagerId'] = request.POST.getlist('createManager')
            data['SPOC_Person'] = request.POST.get('createSPOC')
            addcreateclientURL =  remoteURL + "ClientMaster/api/createClient"
            clientdata = requests.post(addcreateclientURL,data=data,headers=headers) 
            crr_resp_ = clientdata.json()
            if crr_resp_['n']==1:
                messages.success(request,crr_resp_['Msg'])
                return redirect('ClientMaster:createclient')
            else:
                messages.error(request,crr_resp_['Msg'])
                return redirect('ClientMaster:createclient')
            
        if request.method == 'POST' and 'update_form' in request.POST:
            ID = request.POST.get('updateid')
            data['ClientId'] = request.POST.get('updateclientname')
            data['Team'] = request.POST.getlist('UpdateTeam')
            data['Client_ManagerId'] = request.POST.getlist('Managers')
            data['SPOC_Person'] = request.POST.get('updatespocperson')

            addcreateclientURL =  remoteURL + "ClientMaster/api/updateCreateClient?ID="+ID
            clientdata = requests.post(addcreateclientURL,data=data,headers=headers) 
            crr_resp_ = clientdata.json()
            if crr_resp_['n']==1:
                messages.success(request,crr_resp_['Msg'])
                return redirect('ClientMaster:createclient')
            else:
                messages.error(request,crr_resp_['Msg'])
                return redirect('ClientMaster:createclient')


        
        else:
            userListUrl = remoteURL + "users/api/userlist"
            employeelistResponse = requests.get(userListUrl, headers=headers)
            employeelistData = employeelistResponse.json()
            
            clientlistURL = remoteURL + "ClientMaster/api/clientlist"
            clientlistResponse = requests.get(clientlistURL, headers=headers)
            clientResponse_ = clientlistResponse.json()

            managerlistURL = remoteURL + "ClientMaster/api/ClientsideManagerlist"
            managerResponse = requests.get(managerlistURL, headers=headers)
            managerResponse_ = managerResponse.json()

            createclientlistURL = remoteURL + "ClientMaster/api/createClientlist"
            createclientResponse = requests.get(createclientlistURL, headers=headers)
            ccResponse_ = createclientResponse.json()
            
            client_project_listURL = remoteURL + "ClientMaster/api/Client_Projectlist"
            client_project_Response = requests.get(client_project_listURL, headers=headers)
            client_project_list_response = client_project_Response.json()
            
            return render(request,'admin/ClientMaster/CreateClient.html',{'clientlist':clientResponse_['data'],
                                                                          'managerlist':managerResponse_['data'],
                                                                          'createclientlist':ccResponse_['data'],
                                                                          'employeelist':employeelistData['data'],
                                                                          'projectlist':client_project_list_response['data']})
    else:
        return redirect('users:login')
    


def Addclient(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['Client_Name'] = request.POST.get('ClientName')
            addclientURL =  remoteURL + "ClientMaster/api/addclient"
            clientdata = requests.post(addclientURL,data=data,headers=headers) 
            clientresp_ = clientdata.json()
            if clientresp_['n']==1:
                messages.success(request,clientresp_['Msg'])
                return HttpResponse(json.dumps(clientresp_),content_type='application/json')
            else:
                messages.error(request,clientresp_['Msg'])
                return HttpResponse(json.dumps(clientresp_),content_type='application/json')
    else:
        return redirect('users:login')
    

def Updateclient(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            clientID = request.POST.get('ClientID')
            data['Client_Name'] = request.POST.get('ClientName')
            updateclientURL =  remoteURL + "ClientMaster/api/updateclient?clientID="+clientID
            clientdata = requests.post(updateclientURL,data=data,headers=headers) 
            clientresp_ = clientdata.json()
            if clientresp_['n']==1:
                messages.success(request,clientresp_['Msg'])
                return HttpResponse(json.dumps(clientresp_),content_type='application/json')
            else:
                messages.error(request,clientresp_['Msg'])
                return HttpResponse(json.dumps(clientresp_),content_type='application/json')

    else:
        return redirect('users:login')

def Deleteclient(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            clientID = request.POST.get('ClientID')
            deleteclientURL =  remoteURL + "ClientMaster/api/deleteclient?clientID="+clientID
            clientdata = requests.post(deleteclientURL,data=data,headers=headers) 
            clientresp_ = clientdata.json()
            if clientresp_['n']==1:
                messages.success(request,clientresp_['Msg'])
                return HttpResponse(json.dumps(clientresp_),content_type='application/json')
            else:
                messages.error(request,clientresp_['Msg'])
                return HttpResponse(json.dumps(clientresp_),content_type='application/json')
            
            
    else:
        return redirect('users:login')
    



def Addclientsidemanager(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['Manager_Name'] = request.POST.get('managername')
            addmanagerURL =  remoteURL + "ClientMaster/api/addClientsideManager"
            managerdata = requests.post(addmanagerURL,data=data,headers=headers) 
            managerresp_ = managerdata.json()
            if managerresp_['n']==1:
                messages.success(request,managerresp_['Msg'])
                return HttpResponse(json.dumps(managerresp_),content_type='application/json')
            else:
                messages.error(request,managerresp_['Msg'])
                return HttpResponse(json.dumps(managerresp_),content_type='application/json')
    else:
        return redirect('users:login')


def updateclientsidemanager(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            ManagerID = request.POST.get('ManagerID')
            data['Manager_Name'] = request.POST.get('managername')
            updatemanagerURL =  remoteURL + "ClientMaster/api/updateClientsideManager?ManagerID="+ManagerID
            managerdata = requests.post(updatemanagerURL,data=data,headers=headers) 
            managerresp_ = managerdata.json()
            
            return HttpResponse(json.dumps(managerresp_),content_type='application/json')
    else:
        return redirect('users:login')
    

def DeleteManager(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        ManagerID = request.POST.get('ManagerID')
        deletemanagerURL =  remoteURL + "ClientMaster/api/deleteClientsideManager?ManagerID="+ManagerID
        managerdata = requests.post(deletemanagerURL,data=data,headers=headers) 
        managerresp_ = managerdata.json()
        
        messages.success(request,managerresp_['Msg'])
        return HttpResponse(json.dumps(managerresp_),content_type='application/json')
    else:
        return redirect('users:login')
    

def Add_createclient(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['ClientId'] = request.POST.get('createclient')
            data['Team'] = request.POST.getlist('Team')
            data['Client_ManagerId'] = request.POST.getlist('createManager')
            data['SPOC_Person'] = request.POST.get('createSPOC')
            addcreateclientURL =  remoteURL + "ClientMaster/api/createClient"
            clientdata = requests.post(addcreateclientURL,data=data,headers=headers) 
            crr_resp_ = clientdata.json()
            
            return HttpResponse(json.dumps(crr_resp_),content_type='application/json')
    else:
        return redirect('users:login')


def update_createclient(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            ID = request.POST.get('ID')
            data['ClientId'] = request.POST.get('ClientId')
            data['Team'] = request.POST.get('Team')
            data['Client_ManagerId'] = request.POST.get('Client_ManagerId')
            data['SPOC_Person'] = request.POST.get('SPOC_Person')

            addcreateclientURL =  remoteURL + "ClientMaster/api/updateCreateClient?ID="+ID
            clientdata = requests.post(addcreateclientURL,data=data,headers=headers) 
            crr_resp_ = clientdata.json()
            
            return HttpResponse(json.dumps(crr_resp_),content_type='application/json')
    else:
        return redirect('users:login')


def delete_createclient(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            ID = request.POST.get('ID')
            addcreateclientURL =  remoteURL + "ClientMaster/api/deleteCreateClient?ID="+ID
            clientdata = requests.post(addcreateclientURL,data=data,headers=headers) 
            crr_resp_ = clientdata.json()
            
            return HttpResponse(json.dumps(crr_resp_),content_type='application/json')
    else:
        return redirect('users:login')


def Event(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        # access = accessToPage(Menu, url)
        # if access == False:
        #     return redirect('users:accessDenied')
        data={}
        if request.method == 'POST' and 'addform' in request.POST:
            data['ClientId'] = request.POST.get("ClientId")
            data['Project'] = request.POST.get("clientproject")
            data['Assign_To']=request.POST.get("Assign_To")
            data['Assign_By']=request.POST.get("Assign_By")
            data['TaskDescription']=request.POST.get("TaskDescription")
            data['TaskValidation'] = request.POST.get("remarkzone")
            bonus = request.POST.get("bonuszone")
            if bonus is None :
                data['Bonus']= False
            else:
                data['Bonus']= request.POST.get("bonuszone")
            data['AddNote']=request.POST.get("extranote")
        
            addeventURL =  remoteURL + "ClientMaster/api/AddEvent"
            eventdata = requests.post(addeventURL,data=data,headers=headers) 
            crr_resp_ = eventdata.json()
            if crr_resp_['n']==1:
                messages.success(request,crr_resp_['Msg'])
                return redirect('ClientMaster:Event')
            else:
                messages.error(request,crr_resp_['Msg'])
                return redirect('ClientMaster:Event')
            
        if request.method == 'POST' and 'updateform' in request.POST:
            
            ID = request.POST.get("eventid")
            data['ClientId'] = request.POST.get("Updateclient")
            data['Project'] = request.POST.get("updateclientproject")
            data['Assign_To']=request.POST.get("UpdateAssign_To")
            data['Assign_By']=request.POST.get("UpdateAssign_By")
            data['TaskDescription']=request.POST.get("UpdateTaskDescription")
            data['TaskValidation'] = request.POST.get("updateremarkzone"+ID)
            
            bonus = request.POST.get("updatebonuszone")
            if bonus is None :
                data['Bonus']= False
            else:
                data['Bonus']= request.POST.get("updatebonuszone")
            data['AddNote']=request.POST.get("Updateextranote")
        
            addeventURL =  remoteURL + "ClientMaster/api/updateEvent?ID="+ID
            eventdata = requests.post(addeventURL,data=data,headers=headers) 
            crr_resp_ = eventdata.json()
            if crr_resp_['n']==1:
                messages.success(request,crr_resp_['Msg'])
                return redirect('ClientMaster:Event')
            else:
                messages.error(request,crr_resp_['Msg'])
                return redirect('ClientMaster:Event')
        
        else:
            
            clientlistURL = remoteURL + "ClientMaster/api/clientlist"
            clientlistResponse = requests.get(clientlistURL, headers=headers)
            clientResponse_ = clientlistResponse.json()

            managerlistURL = remoteURL + "ClientMaster/api/ClientsideManagerlist"
            managerResponse = requests.get(managerlistURL, headers=headers)
            managerResponse_ = managerResponse.json()

            createclientlistURL = remoteURL + "ClientMaster/api/createClientlist"
            createclientResponse = requests.get(createclientlistURL, headers=headers)
            ccResponse_ = createclientResponse.json()

            eventlistURL = remoteURL + "ClientMaster/api/Eventlist"
            eventlistURLResponse = requests.get(eventlistURL, headers=headers)
            eventResponse_ = eventlistURLResponse.json() 

            return render(request,'admin/ClientMaster/Events.html',{'clientlist':clientResponse_['data'],'managerlist':managerResponse_['data'],'createclientlist':ccResponse_['data'],'eventlist':eventResponse_['data']})
    else:
        return redirect('users:login')
    

def getclientdata(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            ID = request.POST.get('ClientID')
            clientURL =  remoteURL + "ClientMaster/api/getCreateClient?ID="+ID
            clientdata = requests.post(clientURL,data=data,headers=headers) 
            crr_resp_ = clientdata.json()
            
            return HttpResponse(json.dumps(crr_resp_),content_type='application/json')
    else:
        return redirect('users:login')


def deleteevent(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
       
        ID = id
        addcreateclientURL =  remoteURL + "ClientMaster/api/deleteEvent?ID="+str(ID)
        clientdata = requests.post(addcreateclientURL,data=data,headers=headers) 
        delcrr_resp_ = clientdata.json()
        if delcrr_resp_['n'] == 1:
            messages.success(request,delcrr_resp_['Msg'])
            return redirect('ClientMaster:Event')
        else:
            messages.error(request,delcrr_resp_['Msg'])
            return redirect('ClientMaster:Event')
    else:
        return redirect('users:login')
    


def Addclient_project(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['Projectname'] = request.POST.get('ProjectName')
            data['Clientid'] = request.POST.get('ClientId')
            addclientprojectURL =  remoteURL + "ClientMaster/api/AddClient_project"
            clientprojectdata = requests.post(addclientprojectURL,data=data,headers=headers) 
            clientprojectresp_ = clientprojectdata.json()
            if clientprojectresp_['n']==1:
                messages.success(request,clientprojectresp_['Msg'])
                return HttpResponse(json.dumps(clientprojectresp_),content_type='application/json')
            else:
                messages.error(request,clientprojectresp_['Msg'])
                return HttpResponse(json.dumps(clientprojectresp_),content_type='application/json')
    else:
        return redirect('users:login')
    
    
def Updateclientproject(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['ClientId'] = request.POST.get('clientid')
            data['ProjectName'] = request.POST.get('projectname')
            id = request.POST.get('id')
            
            updateclientprojectURL =  remoteURL + "ClientMaster/api/updateClient_project?clientprojectID="+id
            clientprojectdata = requests.post(updateclientprojectURL,data=data,headers=headers) 
            clientprojectresp_ = clientprojectdata.json()
            if clientprojectresp_['n']==1:
                messages.success(request,clientprojectresp_['Msg'])
                return HttpResponse(json.dumps(clientprojectresp_),content_type='application/json')
            else:
                messages.error(request,clientprojectresp_['Msg'])
                return HttpResponse(json.dumps(clientprojectresp_),content_type='application/json')

    else:
        return redirect('users:login')
    

def deleteclientproject(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            id = request.POST.get('id')
            deleteclientURL =  remoteURL + "ClientMaster/api/deleteclientproject?id="+id
            clientdata = requests.post(deleteclientURL,data=data,headers=headers) 
            clientresp_ = clientdata.json()
            if clientresp_['n']==1:
                messages.success(request,clientresp_['Msg'])
                return HttpResponse(json.dumps(clientresp_),content_type='application/json')
            else:
                messages.error(request,clientresp_['Msg'])
                return HttpResponse(json.dumps(clientresp_),content_type='application/json')
            
            
    else:
        return redirect('users:login')