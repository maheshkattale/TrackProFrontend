from django.shortcuts import render,redirect
from django.contrib import messages
from Users.views import remoteURL
import requests
from django.http.response import HttpResponse,HttpResponseRedirect
import json
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from Users.views import accessToPage,accessDenied,statuscheck,checksession


projectListURL = remoteURL + 'project/api/allProjectList'
paginationprojectListURL = remoteURL + 'project/api/paginationprojectlist'
listprojectURL = remoteURL + "project/api/projectLists"
userListUrl = remoteURL + "users/api/userlist"
projectaddURL = remoteURL + "project/api/addproject"
projectdeleteURL = remoteURL + "project/api/deleteproject"
updateProjectURL = remoteURL + "project/api/updateproject"
projectDetailUrl = remoteURL + "checktrackpro/api/report_by_project"
projectnewDetailUrl = remoteURL + "project/api/projectreport"
projecttotaltimeUrl = remoteURL + "project/api/projectreporttotaltasktime"
searchprojectUrl = remoteURL + "project/api/searchproject"
excelprojectnewDetailUrl = remoteURL + "project/api/excelprojectreport"
departmentUrl = remoteURL + "department/api/departmentlist"
# Create your views here.



def projectlist(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "GET":
            # projectlistreponse = requests.get(projectListURL,headers=headers)   
            # projectdata = projectlistreponse.json()
            # listprojectreponse = requests.get(listprojectURL,headers=headers)   
            # liistprojectdata = listprojectreponse.json()
            employeelistResponse = requests.get(userListUrl, headers=headers)
            employeelistData = employeelistResponse.json()
            return render(request, 'admin/masters/project.html',{'employeelist':employeelistData['data']})
        else:
            data={}
            data['ProjectName'] = request.POST.get('ProjectName')
            data['ProjectBA'] = request.POST.get('ProjectBA')
            data['ProjectCoordinator'] = request.POST.getlist('ProjectCoordinator')
            projectaddreponse = requests.post(projectaddURL,headers=headers,data=data)   
            projectdata = projectaddreponse.json()
            if projectdata['n'] == 1:
                messages.success(request,projectdata['Msg'])
                return redirect ('project:projectlist')
            else:
                messages.error(request,projectdata['Msg'])
                return redirect ('project:projectlist')
    else:
        return redirect('users:login')


def baseprojectlist(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        projectListURL = remoteURL + 'project/api/queryprojectlist'
        projectlistreponse = requests.get(projectListURL,headers=headers)   
        projectdata = projectlistreponse.json()
        return HttpResponse(json.dumps(projectdata), content_type="application/json")






def updateproject(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data ={}
        projectId = request.POST.get('projectID')
        data['ProjectName'] = request.POST.get('ProjectName')
        data['ProjectBA'] = request.POST.get('ProjectBA')
        data['ProjectCoordinator'] = json.loads(request.POST.get('ProjectCoordinator'))
        updateProjectStringUrl = updateProjectURL + "?projectID=" + str(projectId)
        updateProjectResponse = requests.post(updateProjectStringUrl, headers=headers,data=data)
        updateProjectData = updateProjectResponse.json()
        
        if updateProjectData['n'] == 1 :
            messages.success(request,updateProjectData['Msg'])
        else:
            messages.error(request,updateProjectData['Msg'])
        return HttpResponse(json.dumps({'data': updateProjectData}), content_type="application/json")
    else:
        return redirect('users:login')



def addProjectTask(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            data = {}
            StartDate = timezone.localtime(timezone.now())
            Task = request.POST['Task']
            data["StartDate"] = StartDate
            data["Task"] = Task
            addprojecttask = requests.post(
                remoteURL+"project/api/addprojecttask", data=data, headers=headers)
            return HttpResponse(json.dumps({'status': '1', 'msg': 'task open'}), content_type="application/json")
    else:
        return redirect('users:login')

@csrf_exempt
def updateProjectTask(request, id):
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data = {}
        if request.method == 'POST':
            EndDate = timezone.localtime(timezone.now())
            data['EndDate'] = EndDate
            updateurl = remoteURL+'tasks/api/closeTaskStatus?id={}'.format(id)
            addTaskResponse = requests.post(updateurl, data=data, headers=headers)
            Response_ = addTaskResponse.json()
            if Response_:
                return HttpResponse(json.dumps({'status': '1', 'msg': 'task closed'}), content_type='application/json')
            else:
                return HttpResponse(json.dumps({'n': 0, }))
    else:
        return redirect('users:login')


@csrf_exempt
def holdProjectTask(request, id):
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data = {}
        if request.method == 'POST':
            EndDate = timezone.localtime(timezone.now())
            data['EndDate'] = EndDate
            updateurl = remoteURL+'tasks/api/holdTaskStatus?id={}'.format(id)
            addTaskResponse = requests.post(updateurl, data=data, headers=headers)
            Response_ = addTaskResponse.json()
            if Response_:
                return HttpResponse(json.dumps(Response_), content_type='application/json')
            else:
                return HttpResponse(json.dumps({'n': 0, }))
    else:
        return redirect('users:login')


@csrf_exempt
def resumeProjectTask(request, id):
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data = {}
        if request.method == 'POST':
            EndDate = timezone.localtime(timezone.now())
            data['EndDate'] = EndDate
            updateurl = remoteURL+'tasks/api/resumeTaskStatus?id={}'.format(id)
            addTaskResponse = requests.post(updateurl, data=data, headers=headers)
            Response_ = addTaskResponse.json()
            if Response_:
                return HttpResponse(json.dumps(Response_), content_type='application/json')
            else:
                return HttpResponse(json.dumps({'n': 0, }))
    else:
        return redirect('users:login')
    
def projectreport(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        access = accessToPage(Menu, url)
        if access == False:
            return redirect('users:accessDenied')
        projectlistreponse = requests.get(projectListURL,headers=headers)   
        projectdata = projectlistreponse.json()

        departmentlistresponse = requests.get(departmentUrl,headers=headers)
        departmentlistdata = departmentlistresponse.json()
        return render(request,'admin/trackproreport/projectrecord.html',{'projectlist':projectdata['data'],'departmentlist':departmentlistdata['data']})
    else:
        return redirect('users:login')


@csrf_exempt
def getProjectDetail(request):
    if request.session.get('PasswordChanged')==False:
        return redirect('users:updatepassword',id=request.session.get('userID'))
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method=="POST":
            data={}
            data['projectName']=request.POST.get('projectName')
            projectDetailRequest=requests.post(projectDetailUrl,data=data,headers=headers)
            projectData=projectDetailRequest.json()
            return HttpResponse(json.dumps(projectData),content_type="application/json")
    else:
        return redirect('users:login')
    

@csrf_exempt
def getnewProjectDetail(request):
    if request.session.get('PasswordChanged')==False:
        return redirect('users:updatepassword',id=request.session.get('userID'))
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method=="POST":
            data={}
            data['projectName']=request.POST.get('projectName')
            data['deptname']=request.POST.get('deptname')
            data['searchname']=request.POST.get('searchname')
            p= request.POST.get('p')
            projectnewDetailUrlpagination = projectnewDetailUrl + "?p=" +str(p)
            projectDetailRequest=requests.post(projectnewDetailUrlpagination,data=data,headers=headers)
            projectData=projectDetailRequest.json()

            projecttotaltimeDetailUrlpagination = projecttotaltimeUrl + "?p=" +str(p)
            projecttimeRequest=requests.post(projecttotaltimeDetailUrlpagination,data=data,headers=headers)
            projecttimeData=projecttimeRequest.json()

            projectData['data']['projecttotalhours'] = projecttimeData['data']['projecttotalhours']

            return HttpResponse(json.dumps(projectData),content_type="application/json")
    else:
        return redirect('users:login')
    



@csrf_exempt
def getProjecttotaltime(request):
    if request.session.get('PasswordChanged')==False:
        return redirect('users:updatepassword',id=request.session.get('userID'))
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method=="POST":
            data={}
            data['projectName']=request.POST.get('projectName')
            data['deptname']=request.POST.get('deptname')
            data['searchname']=request.POST.get('searchname')
            p= request.POST.get('p')
            projecttotaltimeDetailUrlpagination = projecttotaltimeUrl + "?p=" +str(p)
            projectDetailRequest=requests.post(projecttotaltimeDetailUrlpagination,data=data,headers=headers)
            projectData=projectDetailRequest.json()
            return HttpResponse(json.dumps(projectData),content_type="application/json")
    else:
        return redirect('users:login')
    

@csrf_exempt
def excelprojectreport(request):
    if request.session.get('PasswordChanged')==False:
        return redirect('users:updatepassword',id=request.session.get('userID'))
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method=="POST":
            data={}
            data['projectName']=request.POST.get('projectName')
            data['deptname']=request.POST.get('deptname')
            data['searchname']=request.POST.get('searchname')
            p= request.POST.get('p')
            projectnewDetailUrlpagination = excelprojectnewDetailUrl 
            projectDetailRequest=requests.post(projectnewDetailUrlpagination,data=data,headers=headers)
            projectData=projectDetailRequest.json()
            return HttpResponse(json.dumps(projectData),content_type="application/json")
    else:
        return redirect('users:login')
    
@csrf_exempt
def paginationprojectlist(request):
    if request.session.get('PasswordChanged')==False:
        return redirect('users:updatepassword',id=request.session.get('userID'))
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method=="POST":
            data={}
            data['projectname']=request.POST.get('projectname')
            p= request.POST.get('p')
            projectnewDetailUrlpagination = paginationprojectListURL + "?p=" +str(p)
            projectDetailRequest=requests.post(projectnewDetailUrlpagination,data=data,headers=headers)
            projectData=projectDetailRequest.json()

            request_ = requests.get(userListUrl,headers=headers)
            response_data = request_.json()
            return HttpResponse(json.dumps({"projectData":projectData,"userlist":response_data}),content_type="application/json")
    else:
        return redirect('users:login')

def searchProjectDetail(request):
    if request.session.get('PasswordChanged')==False:
        return redirect('users:updatepassword',id=request.session.get('userID'))
    tok = request.session.get('token',False)
    if tok:
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method=="POST":
            data={}
            data['project']=request.POST.get('project')
            projectDetailRequest=requests.post(searchprojectUrl,data=data,headers=headers)
            projectData=projectDetailRequest.json()
            return HttpResponse(json.dumps(projectData),content_type="application/json")
    else:
        return redirect('users:login')
    




def delete_project(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['projectID']=id
        delete_request = requests.post(projectdeleteURL, headers=headers,data=data)
        delete_response = delete_request.json()
        messages.success(request,delete_response['Msg'])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('users:login')
    

def userdashboardlisting(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        projectListURL = remoteURL + 'project/api/queryuserdashboardlist'
        projectlistreponse = requests.get(projectListURL,headers=headers)   
        projectdata = projectlistreponse.json()
        return HttpResponse(json.dumps(projectdata), content_type="application/json")
    else:
        return redirect('users:login')

    
def projectstasks(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}

        return render(request, 'admin/project/projectstasks.html',{})
    else:
        return redirect('users:login')