from django.shortcuts import render,redirect
from django.contrib import messages
from Users.views import remoteURL
import requests
from django.http.response import HttpResponse
import json
import datetime
from datetime import date as date_today  # Renamed to avoid conflict
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from Users.views import accessToPage,accessDenied,checksession

ManagerUserListUrl = remoteURL + "users/api/ManagerUserListAPI"
userListUrl = remoteURL + "users/api/userlist"
tasklistURL =remoteURL + "tasks/api/taskListApi"
taskcordinatorList = remoteURL + "tasks/api/task_cordinator"
employeeTaskList = remoteURL + "tasks/api/get_employeetask"
employeeManagerURL =remoteURL + "tasks/api/get_employeemanager"
allProjectList = remoteURL + "project/api/allProjectList"
manageremplistURL = remoteURL + "users/api/getMappingForUpdate"
dataruleslisturl = remoteURL + "rules/dataruleslist"
updateTaskZoneurl = remoteURL + "tasks/api/updateTaskZone"
addtaskremarkurl = remoteURL + "tasks/api/manager_remark"
addemployeetaskremarkurl = remoteURL + "tasks/api/employee_remark"
taskremarklisturl = remoteURL + "tasks/api/task_remark_list"
dashboardtaskremarklisturl = remoteURL + "tasks/api/dashboardtask_remark_list"

def usertasklist(request):
    tok = request.session.get('token',False)
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 
    if tok:
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        
        userID = request.session.get('userID')
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        access = accessToPage(Menu, url)
        if access == False:
            return redirect('users:accessDenied')
        
        weekdata = {}
        current_date = date_today.today()  # Use renamed import
        day = current_date.day
        month = current_date.month
        year = current_date.year
        w = datetime.datetime(year,month, day)
        print("w1",w)
        
        week = w.isocalendar()[1]
        weekdata['AssignTo'] = userID
        weekdata['Year'] = year
        weekdata['Week'] = week
        w = datetime.datetime.now()
        print("w2",w)
        
        currYear = w.year
        print("currYear",currYear)

        yearreqURL = remoteURL+'tasks/api/yearList'
        yearExcludeResponse = requests.get(yearreqURL, headers=headers)
        yearresponse = yearExcludeResponse.json()
        print("yearresponse1",yearresponse)


        if currYear not in [dict_['Year'] for dict_ in yearresponse]:
            yearresponse.append({'Year':currYear})
            
            
        print("yearresponse2",yearresponse)
            
        print("currYear2",currYear)
        
        
        
        my_date = datetime.date.today()
        year, week_num, day_of_week = my_date.isocalendar()
        currweek = week_num
        context={
            'year':yearresponse,
            'userID':userID,
            'currentweek':currweek,
            # 'project':projectdata['data']
            }
        return render(request,"admin/task/usertasks.html",context)
    else:
        return redirect('users:login')

def get_project_list(request):

    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method=="POST":
            
            get_project_list_Url = remoteURL+"project/api/allProjectList"
            get_project_list_request = requests.get(get_project_list_Url,headers = headers)
            get_project_list_response = get_project_list_request.json()
        return HttpResponse(json.dumps(get_project_list_response), content_type="application/json")
    else:
        return redirect('users:login')
    
    
def addTaskAjax(request):
    tok = request.session.get('token',False)
    if tok:
        data={}

        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}

        if request.method =='POST':
            TaskTitle = request.POST['TaskTitle']
            Project = request.POST['Project']
            Day = request.POST['Day']
            AssignDate = request.POST['AssignDate']
            AssignBy = request.POST['AssignBy']
         
            # helpTaken = request.POST.get('helpTaken',None)
            #day
            # AssignDate="01/01/2025"
            day = int(AssignDate.split('/')[0])
            #month
            month = int(AssignDate.split('/')[1])
            #year
            year = int(AssignDate.split('/')[2])
            #week
            w = datetime.datetime(year,month, day)
            print("w",w)
            week = w.isocalendar()[1]
            newAssignDate = str(year) + '-' + str(month) + '-' + str(day)
            print("week",week)

            

            
            data["TaskTitle"]=TaskTitle
            data["Project"]=Project
            data["Day"]=Day
            data["AssignDate"]=newAssignDate
            data["Year"]=year
            data["Week"]=week
            data["AssignBy"]=AssignBy
            UserId = request.session['userID']
            chwar = {'Employee':UserId,'Year':year,'Week':week}
            chkIfTrackProExists = requests.post(remoteURL+"checktrackpro/api/checktrackproscoreexists",data= chwar,headers = headers)
            warExists = chkIfTrackProExists.json()
            print("warExists['n']",warExists['n'])
            if warExists['n'] == 0:
                return HttpResponse(json.dumps(warExists), content_type="application/json")
            else:
                response = requests.post(remoteURL+"tasks/api/addNewTask",data= data,headers = headers)
                task = response.json()
                if task['n'] == 1 :
                    assign_date = task['data']["AssignDate"]  # Renamed variable
                    currdate = assign_date.split('-')
                    dateDay = int(currdate[2])
                    dateMonth = currdate[1]
                    datetime_object = datetime.datetime.strptime(dateMonth, "%m")
                    month_name = datetime_object.strftime("%B")
                    dateYear = currdate[0]
                    newAssignDate = str(dateDay) + ' ' + str(month_name) + ' ' + str(dateYear)
                    task['data']['AssignDate'] = newAssignDate
               
                    return HttpResponse(json.dumps(task), content_type="application/json")
                else:
                    return HttpResponse(json.dumps(task), content_type="application/json")
    else:
        return redirect('users:login')

def Add_duplicateTask(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}

        if request.method =='POST':
            data['taskID'] = request.POST.get("Taskid")
            duplicateURL = remoteURL+"tasks/api/addduplicatetask"
            response = requests.post(duplicateURL,data= data,headers = headers)
            dupltask = response.json()

            return HttpResponse(json.dumps(dupltask), content_type="application/json")
    else:
        return redirect('users:login')

def Add_Continuetask(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}

        if request.method =='POST':
            data['taskID'] = request.POST.get("Taskid")
            taskcontinueURL = remoteURL+"tasks/api/AddContinuetask"
            response = requests.post(taskcontinueURL,data= data,headers = headers)
            conttask = response.json()

            return HttpResponse(json.dumps(conttask), content_type="application/json")
    else:
        return redirect('users:login')

def usercurrentweektask(request):
    tok = request.session.get('token',False)
    if tok:
        userID = request.session.get('userID')
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        weekdata = {}
        current_date = date_today.today()  # Use renamed import
        ajaxyear = request.POST.get('year')
        ajaxweek =json.loads(request.POST.get('week'))
        ajaxtaskstatus = request.POST.get('Task')
        ajaxreview = request.POST.get('Review')

        if ajaxyear is not None and ajaxyear != "":
            year = int(ajaxyear)
        else:
            year = current_date.year
        day = current_date.day
        #month
        month = current_date.month
        #year
        
        #week
        w = datetime.datetime(year,month, day)
        week = w.isocalendar()[1]
        weekdata['AssignTo'] = userID
        weekdata['Year'] = year
        weekdata['Zone'] = ajaxreview  
        
        if ajaxtaskstatus == "All":
            weekdata['Status'] = [1,2,3]
        elif ajaxtaskstatus == "InProcess":
            weekdata['Status'] = [1,2]
        else :
            weekdata['Status'] = [3]
            
        weekdata['Week']= ajaxweek
        
        userweektaskUrl = remoteURL + "tasks/api/getTaskByDate"
        userweekrequest = requests.post(userweektaskUrl,data=weekdata,headers=headers)
        userweekresponse = userweekrequest.json()
        return HttpResponse(json.dumps(userweekresponse), content_type="application/json")
    else:
        return redirect('users:login')

def employee_record(request):
    tok = request.session.get('token',False)
    if tok:
        userID = request.session.get('userID')
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        access = accessToPage(Menu, url)
        if access == False:
            return redirect('users:accessDenied')
        excludeTrackProUrl = remoteURL+'checktrackpro/api/excludeUserData?userID={}'.format(userID)
        ExcludeResponse = requests.get(excludeTrackProUrl, headers=headers)
        if ExcludeResponse: 
            tasklistResponse = requests.get(tasklistURL, headers=headers)
            tasklist=tasklistResponse.json()
            mylist = sorted(tasklist, key=lambda k: (k['Firstname']))
            Combined = ExcludeResponse.json()
            for t in Combined['results']['TaskMaster']:
                assign_date = t['AssignDate']  # Renamed variable
                currdate = assign_date.split('-')
                dateDay = currdate[2]
                dateMonth = currdate[1]
                dateYear = currdate[0]
                newAssignDates = str(dateDay) + '/' + str(dateMonth) + '/' + str(dateYear)
                t['AssignDate'] = newAssignDates
            w = datetime.datetime.now()
            currYear = w.year
            if currYear not in [dict_['Year'] for dict_ in Combined["results"]["year"]]:
                Combined["results"]["year"].append({'Year':currYear})
            context = {'True':True,'combined':Combined,"uniquetasklist":mylist}
            return render(request,"admin/task/record.html",context)
    else:
        return redirect('users:login')

def taskcoordinator(request):
    tok = request.session.get('token',False) 
    if tok:
        userID = request.session.get('userID')
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        access = accessToPage(Menu, url)
        if access == False:
            return redirect('users:accessDenied')
        response2 = requests.get(userListUrl, headers = headers)
        users = response2.json()
        coordiantorResponse = requests.get(taskcordinatorList,headers=headers)
        coordinatorlist=coordiantorResponse.json()
        return render(request,'admin/task/taskcoordinator.html',{'coordiantorList':coordinatorlist['Coordinator'],'users':users['data']})
    else:
        return redirect('users:login')

def employee_task(request,id):
    assignId = id
    tok = request.session.get('token',False) 
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}        
        response2 = requests.get(userListUrl, headers = headers)
        users = response2.json()
        assignUrl = employeeTaskList + "?assignId=" + str(assignId)
        coordiantorResponse = requests.get(assignUrl,headers=headers)
        coordinatorlist=coordiantorResponse.json()
        return render(request,'admin/task/employee_task.html',{'employeeTaskCount':coordinatorlist['employeeTask'],'users':users['data'],'assignedBy':assignId})
    else:
        return redirect('users:login')

def taskTrackProcoordinator(request):


    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 
    if request.session.get('PasswordChanged')==False:
        return redirect('users:updatepassword',id=request.session.get('userID'))
    tok = request.session.get('token',False) 
    if tok is not None:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        userID = request.session['userID']   
        managerid=userID

        rules_request = requests.get(dataruleslisturl,headers=headers)
        rules_response = rules_request.json()
       
        context = {
            'True':True,
            'managerid':managerid,
            'markslist':rules_response['marks'],

            }
        return render(request,  'admin/task/trackproreport.html', context)
        
    else:
        return redirect('users:login')


def getyearlist(request):
    tok = request.session['token']
    if tok :
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t,"content-type": "application/json"}
        
        if request.method == 'POST':
            w = datetime.datetime.now()
            currYear = w.year
            yearreqURL = remoteURL+'tasks/api/yearList'
            yearExcludeResponse = requests.get(yearreqURL, headers=headers)
            yearresponse = yearExcludeResponse.json()

            if currYear not in [dict_['Year'] for dict_ in yearresponse]:
                yearresponse.append({'Year':currYear})
                
            if yearresponse:
                return HttpResponse(json.dumps({'yearlist':yearresponse,}), content_type ='application/json')
            else:
                return HttpResponse(json.dumps({'n':0,})) 
    else:
        return redirect('users:login')

def getweeklist(request):
    tok = request.session['token']
    if tok :
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t,"content-type": "application/json"}
        
        if request.method == 'POST':
            w = datetime.datetime.now()
            currYear = w.year
            my_date = datetime.date.today()
            year, week_num, day_of_week = my_date.isocalendar()
            currweek = week_num
            prevweek = currweek-1

            weekreqURL = remoteURL+'tasks/api/weekList?year={}'.format(currYear)
            weekExcludeResponse = requests.get(weekreqURL, headers=headers)
            weeksersponse = weekExcludeResponse.json()

            if currweek not in [dict_['Week'] for dict_ in weeksersponse]:
                weeksersponse.append({'Week':currweek})
                weeksersponse.sort(reverse=True, key=myFunc)
                
            if weeksersponse:
                return HttpResponse(json.dumps({'weeklist':weeksersponse,}), content_type ='application/json')
            else:
                return HttpResponse(json.dumps({'n':0,})) 
    else:
        return redirect('users:login')

def getemployeelist(request):
    tok = request.session['token']
    if tok :
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t,"content-type": "application/json"}
        
        if request.method == 'POST':
            tasklistResponse = requests.get(tasklistURL, headers=headers)
            tasklist=tasklistResponse.json()

                
            if tasklist:
                return HttpResponse(json.dumps({'employeelist':tasklist,}), content_type ='application/json')
            else:
                return HttpResponse(json.dumps({'n':0,})) 
    else:
        return redirect('users:login')

def getsupervisorlist(request):
    tok = request.session['token']
    if tok :
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t,"content-type": "application/json"}
        
        if request.method == 'POST':
            userID = request.session['userID']   
            Firstname = request.session.get('Firstname')
            Lastname = request.session.get('Lastname')     
            managerid=userID

            mappinglistResponse = requests.get(ManagerUserListUrl, headers=headers)
            mappinglistData = mappinglistResponse.json()
            


            
            managerlistdata = []
            for i in mappinglistData["data"]:
                managerdict = {
                    "ManagerID":i['ManagerID'],
                    "ManagerIDStr": i['ManagerIDStr']
                }
                managerlistdata.append(managerdict)
            
            for index in range(len(managerlistdata)):
                if managerlistdata[index]['ManagerID'] == userID:
                    del managerlistdata[index]
                    break





            managerlistdata = []
            for i in mappinglistData["data"]:
                managerdict = {
                    "ManagerID":i['ManagerID'],
                    "ManagerIDStr": i['ManagerIDStr']
                }
                managerlistdata.append(managerdict)
            
            if userID in [dict_['ManagerID'] for dict_ in managerlistdata]:
                for index in range(len(managerlistdata)):
                    if managerlistdata[index]['ManagerID'] == userID:
                        del managerlistdata[index]
                        break

                managerfinallist = managerlistdata.insert(0,{
                    "ManagerID":userID,
                    "ManagerIDStr":Firstname + " " + Lastname
                    
                })
                
            
            if mappinglistData:
                return HttpResponse(json.dumps({'managerList':managerlistdata,
            'managerid':managerid,}), content_type ='application/json')
            else:
                return HttpResponse(json.dumps({'n':0,})) 
    else:
        return redirect('users:login')




def updateTaskZoneMultiple(request):
    tok = request.session['token']
    if tok :
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t,"content-type": "application/json"}
        
        if request.method == 'POST':
            data2 = {}
            data = request.POST.get('values')
           
            data2["Year"]=request.POST.get('Year')       
            data2["Employee"] = request.POST.get('Employee')
            data2["Week"] = request.POST.get('Week')
            URL =remoteURL+ 'tasks/api/updateTaskZoneMultiple'
            tasksubmitUrl = remoteURL+ 'checktrackpro/api/getTaskSubmit'  
            Response_ = requests.post(URL, data = json.dumps(data) ,headers = headers)
            
            tasksubmitresponse = requests.post(tasksubmitUrl, data = json.dumps(data2) ,headers = headers)
            convertsubmitresponse = tasksubmitresponse.json()
            if Response_:
                return HttpResponse(json.dumps({'submitdata': convertsubmitresponse}), content_type ='application/json')
            else:
                return HttpResponse(json.dumps({'n':0,})) 
    else:
        return redirect('users:login')


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return ("%d:%02d:%02d HRS" % (hour, minutes, seconds))
 

def updatezone_Tasklist(request):
    tok = request.session['token']
    if tok :
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t,"content-type": "application/json"}
        
        if request.method == 'POST':
            data2 = {}
            data = request.POST.get('values')
            data2["Year"]=request.POST.get('Year')       
            data2["Week"] = request.POST.get('Week')
            URL =remoteURL+ 'tasks/api/updateTaskZoneMultiple'
            Response_ = requests.post(URL, data = json.dumps(data) ,headers = headers)
            finalresp = Response_.json()
            return HttpResponse(json.dumps(finalresp), content_type ='application/json')
            
    else:
        return redirect('users:login')
    



def userdashboard(request):
    tok = request.session.get('token', False)
    if tok:
        if checksession(request):
            messages.error(request,'Session expired !')
            return redirect ('users:login') 
        return render(request,  'admin/task/userdashboard.html')
    else:
        return redirect('users:login')



def activeUsers_dashboard(request):
    if request.session.get('PasswordChanged') == False:
        return redirect('updatepassword/{}/'.format(request.session.get('userID')))
    tok = request.session.get('token', False)
    if tok:
        # get token
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        # get
        UserId = request.session['userID']
        data = {'userID': UserId}

        # response2 = requests.get(userListUrl, headers=headers)         
        # users = response2.json()

        userdashboardURL = remoteURL+'users/api/usersdashboard'
        userDashboard = requests.post(userdashboardURL, data=data, headers=headers)
        dashboard = userDashboard.json()
        # for u in dashboard['UserDashboard']:
        #     if not u[3] and not u[4] and not u[8]:
        #         u[3] = "--"
        #         u[4] = "--"
        #         u[8] = "--"
        #     elif u[8] is not None:
        #         u[8] = convert(u[11])
        return HttpResponse(json.dumps(dashboard), content_type='application/json')
                # return render(request, 'users_dashboard.html',{'Fullname':Fullname,'users':users,'Menu':Menu,'getCurrUserdata':getCurrUserdata,'userdashboard':dashboard['UserDashboard'],'UserId':UserId})
            
    else:
        return redirect('users:login')

def ThreeParamData(request):
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t,"content-type": "application/json"}
        if request.method == 'POST':
            userID = request.session.get('userID')
            Year = request.POST.get('Year',False)
            Week = request.POST.get('Week',False)
            data = {'userID':userID,'Year':Year,'Week':Week}
            URL =remoteURL+ 'tasks/api/ThreeParamTaskData'
            Response_ = requests.post(URL, data = json.dumps(data) ,headers = headers)
            respons_json = Response_.json()
            w = datetime.datetime.now()
            currYear = w.year
            week = w.isocalendar()[1]+1
            if respons_json:
                for t in respons_json:
                        assign_date = t['AssignDate']  # Renamed variable
                        currdate = assign_date.split('-')
                        dateDay = int(currdate[2])
                        dateMonth = currdate[1]
                        datetime_object = datetime.datetime.strptime(dateMonth, "%m")
                        month_name = datetime_object.strftime("%B")
                        dateYear = currdate[0]
                        newAssignDate = str(dateDay) + ' ' + str(month_name) + ' ' + str(dateYear)
                        t['AssignDate'] = newAssignDate  
                
                return HttpResponse(json.dumps({'tasks':respons_json,'currentWeek':week, 'currentYear':currYear}), content_type ='application/json')
            else:
                return HttpResponse(json.dumps({'tasks':[],'currentWeek':week,'currentYear':currYear}), content_type ='application/json')
    else:
        return redirect('users:login')       

################################## delete task #############################################
@csrf_exempt
def deleteTask(request,id): 
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}

        deleteurl = remoteURL+"tasks/api/deleteTask?taskID={}".format(id)
        deleteTaskResponse = requests.post(deleteurl,headers =headers)
        Response_ = deleteTaskResponse.json()
        if Response_:
            return HttpResponse(json.dumps(Response_), content_type ='application/json')

        else:
            return HttpResponse(json.dumps(Response_), content_type ='application/json')

    else:
        return redirect('users:login')

####################################  update task  ##########################################

def getTaskInfo(request,id): 
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}

        gettaskurl = remoteURL+"tasks/api/gettaskbyid"+"/"+str(id)
        editTaskResponse = requests.get(gettaskurl,headers=headers)
        taskresp = editTaskResponse.json()
        return HttpResponse(json.dumps(taskresp), content_type="application/json")
    else:
        return redirect('users:login')



def updateTaskAjax(request,id):
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        data ={}
        if request.method == 'POST':
            Project = request.POST['editProject']
            ProjectName = request.POST['editProjectName']
            TaskTitle = request.POST['editTaskTitle']        
            AssignBy = request.POST['editAssignBy']

            data["TaskTitle"]=TaskTitle
            data["AssignBy"]=AssignBy
            data["Project"]=Project
            data["ProjectName"]=ProjectName

            updateurl = remoteURL+'tasks/api/updateTask?taskID={}'.format(id)
            addTaskResponse = requests.post(updateurl, data = data,headers = headers)
            Response_ = addTaskResponse.json()
            if Response_:
                return HttpResponse(json.dumps(Response_), content_type ='application/json')
            else:
                return HttpResponse(json.dumps({'n':0,}))
    else:
        return redirect('users:login')



######################################## manager to employee task ######################

# def manageremployeelist(request):
#     tok = request.session.get('token', False)
#     if tok:
#         t = 'Token {}'.format(tok)
#         headers = {'Authorization': t}
#         userID = request.session.get('userID')
#         empurl = remoteURL+'users/api/getMappingForUpdate?ManagerID={}'.format(userID)
#         emplistreponse = requests.get(empurl,headers=headers)   
#         empdata = emplistreponse.json()
#         return render(request, 'admin/task/manageremplist.html',{'emplist':empdata['data']})
#     else:
#         return redirect('users:login')
    

# def viewemployeetask(request,id):
#     tok = request.session.get('token',False)
#     if tok:
#         tok = request.session['token']
#         t = 'Token {}'.format(tok) 
#         headers = {'Authorization': t}
#         loggedinmanagerid  = request.session.get('userID')
#         userID=id
#         getTaskByUserURL=remoteURL+'tasks/api/search?userID={}'.format(userID)
#         getTasksResponse = requests.get(getTaskByUserURL, headers = headers)
#         UsersURLs = remoteURL + "tasks/api/assignUserTask?userID={}".format(userID)
#         taskmappingURL = remoteURL+'users/api/getmapping?userID={}'.format(userID)
#         taskmappingresponse = requests.get(taskmappingURL, headers = headers)
#         taskmappingdata = taskmappingresponse.json()
#         weekdata = {}
#         current_date = date_today.today()  # Use renamed import
#         day = current_date.day
#         #month
#         month = current_date.month
#         #year
#         year = current_date.year
#         #week
#         w = datetime.datetime(year,month, day)
#         week = w.isocalendar()[1]
#         weekdata['AssignTo'] = userID
#         weekdata['Year'] = year
#         weekdata['Week'] = week
#         userweektaskUrl = remoteURL + "tasks/api/getTaskByDate"
#         userweekrequest = requests.post(userweektaskUrl,data=weekdata,headers=headers)
#         userweekresponse = userweekrequest.json()

#         #get current year
#         w = datetime.datetime.now()
#         currYear = w.year
#         userListResponse = requests.get(UsersURLs, headers = headers)
#         combinedResponseOfUser = remoteURL+'tasks/api/GetUserTaskData?userID={}'.format(userID) 
#         CombinedResponse = requests.get(combinedResponseOfUser, headers=headers)      
#         if getTasksResponse and userListResponse and CombinedResponse:
#             tasks = getTasksResponse.json()
#             users = userListResponse.json()  
#             Combined = CombinedResponse.json()
#             for t in Combined['results']['TaskMaster']:
#                 assdate = t['AssignDate']
#                 currdate = assdate.split('-')
#                 dateDay = currdate[2]
#                 dateMonth = currdate[1]
#                 dateYear = currdate[0]
#                 newAssignDates = str(dateDay) + '/' + str(dateMonth) + '/' + str(dateYear)
#                 t['AssignDate'] = newAssignDates 
#             if currYear not in [dict_['Year'] for dict_ in Combined["results"]["year"]]:
#                 Combined["results"]["year"].insert(0,{'Year':currYear})
#             return render(request,"admin/task/manageremptask.html",{'loggedManagerid':loggedinmanagerid,'userId':userID,'year':Combined["results"]["year"],'tasks':Combined["results"]["TaskMaster"],'managerlist':taskmappingdata['data'],'project':Combined["results"]["ProjectMaster"],'userID':userID,'userweektasklist':userweekresponse})
#     else:
#         return redirect('users:login')


def manageremptask(request):
        if checksession(request):
            messages.error(request,'Session expired !')
            return redirect ('users:login') 
        tok = request.session.get('token',False)
        if tok:
            tok = request.session['token']
            t = 'Token {}'.format(tok) 
            headers = {'Authorization': t}
            Menu = request.session['Menu']
            url = request.path
            access = accessToPage(Menu, url)
            if access == False:
                return redirect('users:accessDenied')
            
            managerid = request.session.get('userID')
            w = datetime.datetime.now()
            currYear = w.year
            # combinedResponseOfUser = remoteURL+'tasks/api/GetmanagerTaskData?managerid={}'.format(managerid) 
            # CombinedResponse = requests.get(combinedResponseOfUser, headers=headers)      
            # if CombinedResponse:
            #     Combined = CombinedResponse.json()
            #     for t in Combined['results']['TaskMaster']:
            #         assdate = t['AssignDate']
            #         currdate = assdate.split('-')
            #         dateDay = currdate[2]
            #         dateMonth = currdate[1]
            #         dateYear = currdate[0]
            #         newAssignDates = str(dateDay) + '/' + str(dateMonth) + '/' + str(dateYear)
            #         t['AssignDate'] = newAssignDates 
            #     if currYear not in [dict_['Year'] for dict_ in Combined["results"]["year"]]:
            #         Combined["results"]["year"].insert(0,{'Year':currYear})

            yearreqURL = remoteURL+'tasks/api/yearList'
            yearExcludeResponse = requests.get(yearreqURL, headers=headers)
            yearresponse = yearExcludeResponse.json()

            if currYear not in [dict_['Year'] for dict_ in yearresponse]:
                yearresponse.append({'Year':currYear})
                
            empurl = remoteURL+'users/api/getMappingForUpdate?ManagerID={}'.format(managerid)
            emplistreponse = requests.get(empurl,headers=headers)   
            empdata = emplistreponse.json()

            
           
            return render(request,"admin/task/manageremptask.html",{'emplist':empdata['data'],'year':yearresponse,'currYear':currYear})
        else:
            return redirect('users:login')

 



def empcurrentweektask(request):
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        taskdata = {}
        current_date = date_today.today()  # Use renamed import

        managerid = request.session.get('userID')

        ajaxyear = request.POST.get('year')
        ajaxweek = json.loads(request.POST.get('week'))
        ajaxuserid=json.loads(request.POST.get('userId'))
        ajaxtaskstatus = request.POST.get('Task')
        ajaxreview = request.POST.get('Review')

        taskdata['AssignTo'] = ajaxuserid
        taskdata['Year'] = ajaxyear
        taskdata['Assigby'] = managerid
        taskdata['Week'] = ajaxweek
        taskdata['Zone'] = ajaxreview 
       

        if ajaxtaskstatus == "All":
            taskdata['Status'] = [1,2,3]
        elif ajaxtaskstatus == "InProcess":
            taskdata['Status'] = [1,2]
        else :
            taskdata['Status'] = [3]


        userweektaskUrl = remoteURL + "tasks/api/getTaskBymanagerDate"
        userweekrequest = requests.post(userweektaskUrl,data=taskdata,headers=headers)
        userweekresponse = userweekrequest.json()
        return HttpResponse(json.dumps(userweekresponse), content_type="application/json")
    else:
        return redirect('users:login')


def checktaskbymanagerUI(request,id):
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        checktaskurl = remoteURL+'tasks/api/checktaskbymanager?ID={}'.format(id)
        chkIfTrackProExists = requests.get(checktaskurl,headers = headers)
        warExists = chkIfTrackProExists.json()
        return HttpResponse(json.dumps(warExists), content_type="application/json")
    else:
        return redirect('users:login')


def addTaskbymanager(request):
    tok = request.session.get('token',False)
    if tok:
        data={}

        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}

        if request.method =='POST':
            TaskTitle = request.POST['TaskTitle']
            Project = request.POST['Project']
            Day = request.POST['Day']
            AssignDate = request.POST['AssignDate']
            AssignBy = request.POST['AssignBy']
            emplid = request.POST['employeeId']
           

            # helpTaken = request.POST.get('helpTaken',None)
            #day
            day = int(AssignDate.split('/')[0])
            #month
            month = int(AssignDate.split('/')[1])
            #year
            year = int(AssignDate.split('/')[2])
            #week
            w = datetime.datetime(year,month, day)
            week = w.isocalendar()[1]
            newAssignDate = str(year) + '-' + str(month) + '-' + str(day)
            
            data["TaskTitle"]=TaskTitle
            data["Project"]=Project
            data["Day"]=Day
            data["AssignDate"]=newAssignDate
            data["Year"]=year
            data["Week"]=week
            data["AssignBy"]=AssignBy
            data["AssignTo"]=emplid
            
            # data["HelpTaken"]=helpTaken
            # UserId = request.session['userID']
            chwar = {'Employee':emplid,'Year':year,'Week':week}
            chkIfTrackProExists = requests.post(remoteURL+"checktrackpro/api/checktrackproscoreexists",data= chwar,headers = headers)
            warExists = chkIfTrackProExists.json()
            if warExists['n'] == 0:
                return HttpResponse(json.dumps(warExists), content_type="application/json")
            else:
                response = requests.post(remoteURL+"tasks/api/addNewTaskbyManager",data= data,headers = headers)
                task = response.json()
                assign_date = task['data']["AssignDate"]  # Renamed variable
                currdate = assign_date.split('-')
                dateDay = int(currdate[2])
                dateMonth = currdate[1]
                datetime_object = datetime.datetime.strptime(dateMonth, "%m")
                month_name = datetime_object.strftime("%B")
                dateYear = currdate[0]
                newAssignDate = str(dateDay) + ' ' + str(month_name) + ' ' + str(dateYear)
                task['data']['AssignDate'] = newAssignDate
               
                return HttpResponse(json.dumps(task), content_type="application/json")
    else:
        return redirect('users:login')
    


def Zonestatusbymanager(request):
    tok = request.session.get('token',False)
    if tok:
        data={}

        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}

        if request.method =='POST':
            zonestatus = request.POST['zonestatus']
            taskId = request.POST['taskId']
           
            data["Zonestatus"]=zonestatus
            data["taskid"]=taskId
          
            response = requests.post(remoteURL+"tasks/api/Zonestatusbymanagerapi",data= data,headers = headers)
            resptask = response.json()
            return HttpResponse(json.dumps(resptask), content_type="application/json")
    else:
        return redirect('users:login')
    

def taskbonusbymanager(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method =='POST':
            taskbonus = request.POST['bonus']
            taskId = request.POST['taskid']
            data["Bonus"]=taskbonus
            data["taskid"]=taskId
            response = requests.post(remoteURL+"tasks/api/taskbonusbymanagerapi",data= data,headers = headers)
            resptask = response.json()
            return HttpResponse(json.dumps(resptask), content_type="application/json")
    else:
        return redirect('users:login')
    
def Employeetaskinfom(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method =='POST':
            data['employeeid'] = request.POST['employeeid']
            data['managerid'] = request.POST['managerid']
            response = requests.post(remoteURL+"tasks/api/employeetaskinfo",data= data,headers = headers)
            resptask = response.json() 
            return HttpResponse(json.dumps(resptask), content_type="application/json")
    else:
        return redirect('users:login')
    
def Managertaskinfom(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method =='POST':
            data['managerid'] = request.POST['managerid']
            response = requests.post(remoteURL+"tasks/api/Managertaskinfomapi",data= data,headers = headers)
            resptask = response.json() 
            return HttpResponse(json.dumps(resptask), content_type="application/json")
    else:
        return redirect('users:login')
    


def ManagerReview(request):
    
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        access = accessToPage(Menu, url)
        if access == False:
            return redirect('users:accessDenied')
        
        userID=request.session.get('userID')
        Firstname = request.session.get('Firstname')
        Lastname = request.session.get('Lastname') 

       
        w = datetime.datetime.now()
        currYear = w.year

        weekreqURL = remoteURL+'tasks/api/weekList?year={}'.format(currYear)
        weekExcludeResponse = requests.get(weekreqURL, headers=headers)
        if weekExcludeResponse.status_code != 200:
            messages.error(request,'Session expired !')
            return redirect ('users:login')
        
        weeksersponse = weekExcludeResponse.json()

        yearreqURL = remoteURL+'tasks/api/yearList'
        yearExcludeResponse = requests.get(yearreqURL, headers=headers)
        yearresponse = yearExcludeResponse.json()

        my_date = datetime.date.today()
        year, week_num, day_of_week = my_date.isocalendar()
        currweek = week_num
        prevweek = currweek-1
        
        if currYear not in [dict_['Year'] for dict_ in yearresponse]:
            yearresponse.append({'Year':currYear})

        if currweek not in [dict_['Week'] for dict_ in weeksersponse]:
            weeksersponse.append({'Week':currweek})
            weeksersponse.sort(reverse=True, key=myFunc)


        mappinglistResponse = requests.get(ManagerUserListUrl, headers=headers)
        mappinglistData = mappinglistResponse.json()

        managerlistdata = []
        for i in mappinglistData["data"]:
            managerdict = {
                "ManagerID":i['ManagerID'],
                "ManagerIDStr": i['ManagerIDStr']
            }
            managerlistdata.append(managerdict)
        
        if userID in [dict_['ManagerID'] for dict_ in managerlistdata]:
            for index in range(len(managerlistdata)):
                if managerlistdata[index]['ManagerID'] == userID:
                    del managerlistdata[index]
                    break

            managerfinallist = managerlistdata.insert(0,{
                "ManagerID":userID,
                "ManagerIDStr":Firstname + " " + Lastname
                
            })
        rules_request = requests.get(dataruleslisturl,headers=headers)
        rules_response = rules_request.json()
        
        return render(request,"admin/task/Manager_Review.html",{'managerlist':managerlistdata,'yearlist':yearresponse,'currentyear':currYear,'prevweek':prevweek,'weeklist':weeksersponse,'userID':userID,'markslist':rules_response['marks']})
    else:
        return redirect('users:login')
    

def listmanagerreview(request):
    
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        # Menu = request.session['Menu']
        # url = request.path
        # access = accessToPage(Menu, url)
        # if access == False:
        #     return redirect('users:accessDenied')
        
        userID=request.session.get('userID')
        Firstname = request.session.get('Firstname')
        Lastname = request.session.get('Lastname') 

       
        w = datetime.datetime.now()
        currYear = w.year

        weekreqURL = remoteURL+'tasks/api/weekList?year={}'.format(currYear)
        weekExcludeResponse = requests.get(weekreqURL, headers=headers)
        if weekExcludeResponse.status_code != 200:
            messages.error(request,'Session expired !')
            return redirect ('users:login')
        
        weeksersponse = weekExcludeResponse.json()
        

        yearreqURL = remoteURL+'tasks/api/yearList'
        yearExcludeResponse = requests.get(yearreqURL, headers=headers)
        yearresponse = yearExcludeResponse.json()

        my_date = datetime.date.today()
        year, week_num, day_of_week = my_date.isocalendar()
        currweek = week_num
        prevweek = currweek-1
        
        if currYear not in [dict_['Year'] for dict_ in yearresponse]:
            yearresponse.append({'Year':currYear})

        if currweek not in [dict_['Week'] for dict_ in weeksersponse]:
            weeksersponse.append({'Week':currweek})
            weeksersponse.sort(reverse=True, key=myFunc)


        mappinglistResponse = requests.get(ManagerUserListUrl, headers=headers)
        mappinglistData = mappinglistResponse.json()

        managerlistdata = []
        for i in mappinglistData["data"]:
            managerdict = {
                "ManagerID":i['ManagerID'],
                "ManagerIDStr": i['ManagerIDStr']
            }
            managerlistdata.append(managerdict)
        
        if userID in [dict_['ManagerID'] for dict_ in managerlistdata]:
            for index in range(len(managerlistdata)):
                if managerlistdata[index]['ManagerID'] == userID:
                    del managerlistdata[index]
                    break

            managerfinallist = managerlistdata.insert(0,{
                "ManagerID":userID,
                "ManagerIDStr":Firstname + " " + Lastname
                
            })
        rules_request = requests.get(dataruleslisturl,headers=headers)
        rules_response = rules_request.json()
        
        return render(request,"admin/task/listmanager_review.html",{'managerlist':managerlistdata,'yearlist':yearresponse,'currentyear':currYear,'prevweek':prevweek,'weeklist':weeksersponse,'userID':userID,'markslist':rules_response['marks']})
    else:
        return redirect('users:login')
    

def myFunc(e):
  return e['Week']  

def ReviewEmployeelist(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method =='POST':
            data['Managerid'] = request.POST['AssignBy']
            data['Year'] = request.POST['Year']
            data['Week'] = request.POST['Week']
            response = requests.post(remoteURL+"tasks/api/employeereviewinfo",data= data,headers = headers)
            resptask = response.json() 
            
            return HttpResponse(json.dumps(resptask), content_type="application/json")
    else:
        return redirect('users:login')


def ReviewEmployeetasklist(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method =='POST':
            data['Managerid'] = request.POST['AssignBy']
            data['Year'] = request.POST['Year']
            data['Week'] = request.POST['Week']
            response = requests.post(remoteURL+"tasks/api/employeetasklistreviewinfo",data= data,headers = headers)
            resptask = response.json()
            return HttpResponse(json.dumps(resptask), content_type="application/json")
    else:
        return redirect('users:login')



def finalsubmitall(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method =='POST':
            data['Managerid'] = request.POST['AssignBy']
            data['Year'] = request.POST['Year']
            data['Week'] = request.POST['Week']
            response = requests.post(remoteURL+"tasks/api/Allemp_finalsubmit",data= data,headers = headers)
            resptask = response.json() 
            
            return HttpResponse(json.dumps(resptask), content_type="application/json")
    else:
        return redirect('users:login')


def Weeklyreport(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 
    tok = request.session.get('token',False)
    if tok:
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        userID = request.session.get('userID')
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        access = accessToPage(Menu, url)
        if access == False:
            return redirect('users:accessDenied')
        
        userListUrl = remoteURL + "users/api/userlist"
        empresponse = requests.get(userListUrl, headers=headers)         
        users = empresponse.json()

        

        yearreqURL = remoteURL+'tasks/api/yearList'
        yearExcludeResponse = requests.get(yearreqURL, headers=headers)
        yearresponse = yearExcludeResponse.json()

        my_date = datetime.date.today()
        year, week_num, day_of_week = my_date.isocalendar()
        currweek = week_num
        prevweek = currweek-1
        currYear = year
        
        weekreqURL = remoteURL+'tasks/api/weekList?year={}'.format(currYear)
        weekExcludeResponse = requests.get(weekreqURL, headers=headers)
        weeksersponse = weekExcludeResponse.json()

        if currYear not in [dict_['Year'] for dict_ in yearresponse]:
            yearresponse.append({'Year':currYear})

        if currweek not in [dict_['Week'] for dict_ in weeksersponse]:
            weeksersponse.append({'Week':currweek})
            weeksersponse.sort(reverse=True, key=myFunc)
        
        return render(request,"admin/task/weeklyreport.html",{'employeelist':users['data'],'Yearlist':yearresponse,'weeklist':weeksersponse,'currentyear':currYear,'prevweek':prevweek})
    else:
        return redirect('users:login')
    

def weeklyreportdata(request):
    tok = request.session.get('token',False)
    if tok:
        userID = request.session.get('userID')
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        data={}

        data['ajaxyear'] = request.POST.get('year')
        data['ajaxweek'] =json.loads(request.POST.get('week'))
        data['ajaxEmployee'] = request.POST.get('Employee')

        userweekdataUrl = remoteURL + "tasks/api/weeklydataapi"
        userweekrequest = requests.post(userweekdataUrl,data=data,headers=headers)
        userweekresponse = userweekrequest.json()
        return HttpResponse(json.dumps(userweekresponse), content_type="application/json")
    else:
        return redirect('users:login')
    
    
def weeklyprojectreportdata(request):
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        data={}

        data['ajaxyear'] = request.POST.get('year')
        data['ajaxweek'] =request.POST.get('week')
        data['ajaxEmployee'] = request.POST.get('Employee')

        userprojectdataUrl = remoteURL + "tasks/api/userweekmodaldata"
        userprojectrequest = requests.post(userprojectdataUrl,data=data,headers=headers)
        userprojectresponse = userprojectrequest.json()
        return HttpResponse(json.dumps(userprojectresponse), content_type="application/json")
    else:
        return redirect('users:login')
    

def previoustasktime(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method =='POST':

            data['Taskid'] = request.POST.get('Taskid')

            tasktimedataUrl = remoteURL + "tasks/api/tasktime"
            taskdatarequest = requests.post(tasktimedataUrl,data=data,headers=headers)
            taskresponse = taskdatarequest.json()
            return HttpResponse(json.dumps(taskresponse), content_type="application/json")
    else:
        return redirect('users:login')

    
def weekdates(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method =='POST':

            data['week'] = request.POST.get('week')
            data['year'] = request.POST.get('year')

            taskweekdatesUrl = remoteURL + "tasks/api/weekdatesapi"
            taskdatarequest = requests.post(taskweekdatesUrl,data=data,headers=headers)
            taskresponse = taskdatarequest.json()
            
            return HttpResponse(json.dumps(taskresponse), content_type="application/json")
    else:
        return redirect('users:login')
    

def EMPWeeklyreport(request):
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        # access = accessToPage(Menu, url)
        # if access == False:
        #     return redirect('users:accessDenied')
        
        userListUrl = remoteURL + "users/api/userlist"
        empresponse = requests.get(userListUrl, headers=headers)         
        users = empresponse.json()

        yearreqURL = remoteURL+'tasks/api/yearList'
        yearExcludeResponse = requests.get(yearreqURL, headers=headers)
        yearresponse = yearExcludeResponse.json()

        w = datetime.datetime.now()
        currYear = w.year


        return render(request,"admin/trackproreport/Empweekdata.html",{'emplist':users['data'],'Yearlist':yearresponse,'currentyear':currYear})
    else:
        return redirect('users:login')
    

def EMPWeeklydata(request):
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        
        if request.method =='POST':
            data={}
            data['empid'] = request.POST.get('empid')
            data['year'] = request.POST.get('year')

            taskweekdatesUrl = remoteURL + "tasks/api/Empweeklywar"
            taskdatarequest = requests.post(taskweekdatesUrl,data=data,headers=headers)
            weekresponse = taskdatarequest.json()
            
            return HttpResponse(json.dumps(weekresponse), content_type="application/json")
    else:
        return redirect('users:login')

def get_taskdetail(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method =='POST':

            data['Taskid'] = request.POST.get('Taskid')
            tasktimedataUrl = remoteURL + "tasks/api/gettaskdetail?taskID=" + str(data['Taskid'])
            taskdatarequest = requests.get(tasktimedataUrl,data=data,headers=headers)
            taskresponse = taskdatarequest.json()
            return HttpResponse(json.dumps(taskresponse), content_type="application/json")
    else:
        return redirect('users:login')

def updateParticularTaskZone(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method =='POST':

            data['Taskid'] = request.POST.get('Taskid')
            data['Zone'] = request.POST.get('Zone')
            tasktimedataUrl = remoteURL + "tasks/api/updateTaskZone?taskID=" + str(data['Taskid'])
            taskdatarequest = requests.post(tasktimedataUrl,data=data,headers=headers)
            taskresponse = taskdatarequest.json()
            return HttpResponse(json.dumps(taskresponse), content_type="application/json")
    else:
        return redirect('users:login')


def addmanagertaskremark(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method =='POST':
            data['user_id'] = request.POST.get('user_id')
            data['remark_comment'] = request.POST.get('remark_comment')
            data['task_id'] = request.POST.get('task_id')
            taskremarkrequest = requests.post(addtaskremarkurl,data=data,headers=headers)
            taskresponse = taskremarkrequest.json()
            return HttpResponse(json.dumps(taskresponse), content_type="application/json")
    else:
        return redirect('users:login')
    

def addemployertaskremark(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method =='POST':
            data['user_id'] = request.POST.get('user_id')
            data['remark_comment'] = request.POST.get('remark_comment')
            data['task_id'] = request.POST.get('task_id')
            taskremarkrequest = requests.post(addemployeetaskremarkurl,data=data,headers=headers)
            taskresponse = taskremarkrequest.json()
            return HttpResponse(json.dumps(taskresponse), content_type="application/json")
    else:
        return redirect('users:login')

def taskremarklist(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method =='POST':
            data['task_id'] = request.POST.get('task_id')
            taskremarklistrequest = requests.post(taskremarklisturl,data=data,headers=headers)
            taskresponse = taskremarklistrequest.json()
            return HttpResponse(json.dumps(taskresponse), content_type="application/json")
    else:
        return redirect('users:login')
    

def dashboardtaskremarklist(request):
    tok = request.session.get('token',False)
    if tok:
        data={}
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method =='POST':
            data['task_id'] = request.POST.get('task_id')
            taskremarklistrequest = requests.post(dashboardtaskremarklisturl,data=data,headers=headers)
            taskresponse = taskremarklistrequest.json()
            return HttpResponse(json.dumps(taskresponse), content_type="application/json")
    else:
        return redirect('users:login')






def getweeklytask(request):
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        
        if request.method =='POST':
            data={}
            data['empid'] = request.POST.get('empid')
            taskweeklydetailsUrl = remoteURL + "tasks/api/weeklytasks"
            taskdatarequest = requests.post(taskweeklydetailsUrl,data=data,headers=headers)
            weekresponse = taskdatarequest.json()
            
            return HttpResponse(json.dumps(weekresponse), content_type="application/json")
    else:
        return redirect('users:login')
    


def search_tasks(request):
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        data={}
        data['start_date'] = request.POST.get('start_date')
        data['end_date'] = request.POST.get('end_date')
        data['Employee'] = request.POST.get('Employee')
        data['ongoingtasks'] = request.POST.get('ongoingtasks')
        userprojectdataUrl = remoteURL + "tasks/api/search_tasks"
        userprojectrequest = requests.post(userprojectdataUrl,data=data,headers=headers)
        userprojectresponse = userprojectrequest.json()
        return HttpResponse(json.dumps(userprojectresponse), content_type="application/json")
    else:
        return redirect('users:login')