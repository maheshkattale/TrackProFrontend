from django.shortcuts import render
from Users.views import remoteURL
from django.shortcuts import render,  HttpResponse, redirect
import requests
import json
import datetime
from Users.views import getfullname,tokenmsg,dashboardURL
from django.views.decorators.csrf import csrf_exempt
from Users.views import accessToPage,accessDenied,checksession
from django.contrib import messages

getLastTaskUrl = remoteURL + "checktrackpro/api/getlasttask"
gettaskUrl = remoteURL + "checktrackpro/api/getTask"
getParticualrEmployeeTaskUrl = remoteURL + "checktrackpro/api/getParticualrEmployeeTask"
gettrackproScoreUrl = remoteURL + "checktrackpro/api/getScore"
gettrackproTaskScoreUrl = remoteURL + "checktrackpro/api/getTaskScore"
combinedTrackProUrl = remoteURL + "tasks/api/GetAllTaskData"
userListUrl = remoteURL + "users/api/userlist"
departmentUrl = remoteURL + "department/api/departmentlist"

def getUserWeek(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        userID = request.session.get('userID')
        data = {}
        if request.method == 'POST':
            year = request.POST['year']
            userID = request.session.get('userID')
            data['Year'] = year
            data['userID'] = userID
            url = remoteURL+'tasks/api/userWeekList'
            Response_ = requests.post(url, data=data, headers=headers)
            weeklistd = Response_.json()
            weeklist = weeklistd['data']

            w = datetime.datetime.now()
            print("w",w)
            
            currYear = w.year
            currweek = w.isocalendar()[1]
            

            
            
            
            
            
            print("currweek",currweek)
            if int(year) == int(currYear):
                if currweek not in [dict_['Week'] for dict_ in weeklist]:
                    weeklist.insert(0, {'Week': currweek})
                    
            response = {'weeklist': weeklist}
            
            return HttpResponse(json.dumps(response), content_type="application/json")
        else:
            return HttpResponse({'n': 0}, content_type="application/json")
    else:
        return redirect('users:login')
    


def getmanagerWeek(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        userID = request.session.get('userID')
        data = {}
        if request.method == 'POST':
            year = request.POST['year']
            userID = request.session.get('userID')
            data['Year'] = year
            data['userID'] = userID
            url = remoteURL+'tasks/api/managertaskWeekList'
            Response_ = requests.post(url, data=data, headers=headers)
            weeklistd = Response_.json()
            weeklist=weeklistd['data']


            w = datetime.datetime.now()
            currYear = w.year
            currweek = w.isocalendar()[1]

            if int(year) == int(currYear):
                if currweek not in [dict_['Week'] for dict_ in weeklist]:
                    weeklist.insert(0, {'Week': currweek})
            response = {'weeklist': weeklist}
            return HttpResponse(json.dumps(response), content_type="application/json")
        else:
            return HttpResponse({'n': 0}, content_type="application/json")
    else:
        return redirect('users:login')
    
def getlastTask(request):
    if request.session.get('PasswordChanged') == False:
        return redirect('users:updatepassword', id=request.session.get('userID'))
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data = {}
            data['employee'] = request.POST.get('employee')
            data['year'] = request.POST.get('year')
            getlastTaskurl = requests.post(
                getLastTaskUrl, data=data, headers=headers)
            getLastTask = getlastTaskurl.json()
            if getLastTask:
                return HttpResponse(json.dumps(getLastTask), content_type="application/json")
            else:
                return HttpResponse(json.dumps(getLastTask), content_type="application/json")
    else:
        return redirect('users:login')

def getAllTask(request):
    if request.session.get('PasswordChanged') == False:
        return redirect('users:updatepassword', id=request.session.get('userID'))
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data = {}
            data['Year'] = request.POST.get('Year')
            data['Week'] = request.POST.get('Week')
            data['Employee'] = request.POST.get('Employee')
            getTaskurl = requests.post(gettaskUrl, data=data, headers=headers)
            taskdata = getTaskurl.json()
            if taskdata['n'] == 1:
                return HttpResponse(json.dumps(taskdata), content_type="application/json")
            else:
                return HttpResponse(json.dumps(taskdata), content_type="application/json")
    else:
        return redirect('users:login')

def getAssignTask(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data = {}
            data['Year'] = request.POST.get('Year')
            data['Week'] = request.POST.get('Week')
            data['Employee'] = request.POST.get('Employee')
            data['AssignBy'] = request.POST.get('AssignBy')
            getTaskurl = requests.post(getParticualrEmployeeTaskUrl, data=data, headers=headers)
            taskdata = getTaskurl.json()
            if taskdata['n'] == 1:
                return HttpResponse(json.dumps(taskdata), content_type="application/json")
            else:
                return HttpResponse(json.dumps(taskdata), content_type="application/json")
    else:
        return redirect('users:login')

def getTaskTrackProScore(request):
    if request.session.get('PasswordChanged') == False:
        return redirect('users:updatepassword', id=request.session.get('userID'))
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data = {}
            data['Week'] = request.POST.get('Week')
            data['Employee'] = request.POST.get('Employee')
            data['Year'] = request.POST.get('Year')
            data['AssignBy'] = request.POST.get('AssignBy')
            getTrackProScoreUrl = requests.post(
                gettrackproTaskScoreUrl, data=data, headers=headers)
            getScore = getTrackProScoreUrl.json()
            if getScore['n'] == 1:
                return HttpResponse(json.dumps(getScore), content_type="application/json")
            else:
                return HttpResponse(json.dumps(getScore), content_type="application/json")
    else:
        return redirect('users:login')

def addParticualrIntermediateTrackProResult(request):
    tok = request.session.get('token', False)
    if tok:
        data = {}
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers1 = {'Authorization': t,"content-type": "application/json"}
        headers2 = {'Authorization': t}

        if request.method == 'POST':
            Employee = request.POST['Employee']
            Week = request.POST['Week']
            Year = request.POST['Year']
           
            data["Employee"] = Employee
            data["Week"] = Week
            data["Year"] = Year
           
            data2 = request.POST.get('values')
            updatezoneURL =remoteURL+ 'tasks/api/updateTaskZoneMultiple'
            Response_ = requests.post(updatezoneURL, data = json.dumps(data2) ,headers = headers1)
            response = requests.post(
                remoteURL+"checktrackpro/api/addParticualrIntermediateTrackProResult", data=data, headers=headers2)
           
            # return redirect('')  this one
            r = response.json()
           
            return HttpResponse(json.dumps(response.json()), content_type="application/json")

    else:
        return redirect('users:login')

def mytrackproscore(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        access = accessToPage(Menu, url)
        if access == False:
            return redirect('users:accessDenied')
        
        userID = request.session['userID']
        combinedResponseOfUser = remoteURL + 'tasks/api/Mytrackproscoredata?userID={}'.format(userID)
        CombinedResponse = requests.get(
            combinedResponseOfUser, headers=headers)
        w = datetime.datetime.now()
        currYear = w.year
        Combined = CombinedResponse.json()
        if currYear not in [dict_['Year'] for dict_ in Combined["results"]['year']]:
            Combined["results"]["year"].insert(0, {'Year': currYear})
        context = {'True': True,'combined': Combined, 'userID': userID}
        return render(request,'admin/trackproreport/mytrackproscore.html',context)
    else:
        return redirect('users:login')

def trackpro_rank(request):
    # if request.session.get('PasswordChanged') == False:
    #     return redirect('users:updatepassword', id=request.session.get('userID'))
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        Fullname = getfullname(request)
        # getCurrUserdata = userforpage(request)
        Menu = request.session['Menu']
        userID = request.session['userID']
        data = {'userID': userID}
        dashboardResponse = requests.post(
            dashboardURL, data=data, headers=headers)
        if dashboardResponse:
            dashboard = dashboardResponse.json()
            context = {'Fullname': Fullname, 'Menu': Menu, 'True': True,
                       'dashboard': dashboard, 'userID': userID, 'getCurrUserdata': "getCurrUserdata"}
            return render(request,   'admin/trackproreport/trackprorank.html', context)
        return HttpResponse(tokenmsg)
    else:
        return redirect('users:login')

# @csrf_exempt
def trackproresult(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 
    if request.session.get('PasswordChanged') == False:
        return redirect('users:updatepassword', id=request.session.get('userID'))
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        Fullname = getfullname(request)
      
        Menu = request.session['Menu']
        url = request.path
        access = accessToPage(Menu, url)
        if access == False:
            return redirect('users:accessDenied')
       
        w = datetime.datetime.now()
        currYear = w.year
        
        yearreqURL =  remoteURL+'tasks/api/yearList'
        yearExcludeResponse = requests.get(yearreqURL, headers=headers)
        yearsersponse = yearExcludeResponse.json()

        employeelistResponse = requests.get(userListUrl, headers=headers)
        employeelistData = employeelistResponse.json()
    
        if currYear not in [dict_['Year'] for dict_ in yearsersponse]:
            yearsersponse.insert(0, {'Year': currYear})

        context = {'Fullname': Fullname, 'Menu': Menu, 'True': True,'employeelist':employeelistData['data'],
                   'yearlist':yearsersponse,'currYear':currYear}
        return render(request,   'admin/trackproreport/Depttrackprorank.html', context)
    else:
        return redirect('users:login')

def depttrackproresult(request):
    if request.session.get('PasswordChanged') == False:
        return redirect('users:updatepassword', id=request.session.get('userID'))
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        Fullname = getfullname(request)
      
        Menu = request.session['Menu']
        url = request.path
        access = accessToPage(Menu, url)

        yearreqURL = remoteURL+'tasks/api/yearList'
        yearExcludeResponse = requests.get(yearreqURL, headers=headers)
        yearresponse = yearExcludeResponse.json()

        w = datetime.datetime.now()
        currYear = w.year

        context = {'Fullname': Fullname, 'Menu': Menu, 'True': True,'yearlist':yearresponse,'currentyear':currYear}
        return render(request,'admin/trackproreport/Depttrackprorank.html', context)
    else:
        return redirect('users:login')

def gettableinfo(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}

        data = {}
        if request.method == 'POST':
            getyear = request.POST.get('Year', None)
      
            my_date = datetime.date.today()
            year, week_num, day_of_week = my_date.isocalendar()
            currweek = week_num
            w = datetime.datetime.now()
            currYear = w.year

            data['year'] = getyear
            weekreqURL =  remoteURL+'tasks/api/weekListbtn'
            weekresponseurl = requests.post(weekreqURL,data=data,headers=headers)
            weekresponse = weekresponseurl.json()

            if getyear == currYear:
                if currweek not in [dict_['Week'] for dict_ in weekresponse]:
                    weekresponse.insert(0, {'Week':currweek})

            # deptlistreponse = requests.get(departmentUrl,headers=headers)   
            # deptdata = deptlistreponse.json()
        
            context = {'weeklist':weekresponse['weeklist'],'deptdata':weekresponse['deptdata']}
            return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return redirect('users:login')

def getweeklyempinfo(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}

        data = {}
        if request.method == 'POST':
            data['getyear'] = request.POST.get('Year', None)
            data['getweek'] = request.POST.get('Week', None)
            data['getdept'] = request.POST.get('departmentid', None)
            
            empweekreqURL =  remoteURL+'tasks/api/getweeklyempinfoapi'
            weekresponseurl = requests.post(empweekreqURL,data=data,headers=headers)
            empweekresponse = weekresponseurl.json()

            return HttpResponse(json.dumps(empweekresponse), content_type="application/json")
    else:
        return redirect('users:login')
    
def getavgempinfo(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}

        data = {}
        if request.method == 'POST':
            data['getdept'] = request.POST.get('departmentid', None)
            
            empavgpercentreqURL =  remoteURL+'tasks/api/overall_week_avg_ny_dept_api'
            avgperresponseurl = requests.post(empavgpercentreqURL,data=data,headers=headers)
            empavgpercentresponse = avgperresponseurl.json()

            return HttpResponse(json.dumps(empavgpercentresponse), content_type="application/json")
    else:
        return redirect('users:login')

def viewweeklyempinfo(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}

        data = {}
        if request.method == 'POST':
            data['getyear'] = request.POST.get('Year', None)
            data['getweek'] = request.POST.get('Week', None)
            data['getdept'] = request.POST.get('departmentid', None)
            
            empweekreqURL =  remoteURL+'tasks/api/viewweeklyempinfoapi'
            weekresponseurl = requests.post(empweekreqURL,data=data,headers=headers)
            empweekresponse = weekresponseurl.json()

            return HttpResponse(json.dumps(empweekresponse), content_type="application/json")
    else:
        return redirect('users:login')

def publishdeptwiserank(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}

        data = {}
        if request.method == 'POST':
            data['getyear'] = request.POST.get('Year', None)
            data['getweek'] = request.POST.get('Week', None)
            data['getdept'] = request.POST.get('departmentid', None)
            
            empweekreqURL =  remoteURL+'tasks/api/publishdeptwiserankapi'
            weekresponseurl = requests.post(empweekreqURL,data=data,headers=headers)
            empweekresponse = weekresponseurl.json()

            return HttpResponse(json.dumps(empweekresponse), content_type="application/json")
    else:
        return redirect('users:login')

@csrf_exempt
def trackproResultWeek(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        userID = request.session['userID']
        data = {}
        if request.method == 'POST':
            year = request.POST.get('year', None)
           

            w = datetime.datetime.now()
            currYear = w.year

            weekreqURL = remoteURL+'tasks/api/weekList?year={}'.format(year)
            weekExcludeResponse = requests.get(weekreqURL, headers=headers)
            weeksersponse = weekExcludeResponse.json()
          
            currweek = w.isocalendar()[1]
            if int(year) == int(currYear):
                if currweek not in [dict_['Week'] for dict_ in weeksersponse]:
                    weeksersponse.insert(0, {'Week': currweek})
            return HttpResponse(json.dumps(weeksersponse), content_type="application/json")
        else:
            return HttpResponse({'n': 0}, content_type="application/json")
    else:
        return redirect('users:login')
    
@csrf_exempt
def Getemployeerankinformation(request):
    tok = request.session['token']
    if tok: 
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            Year = request.POST.get('Year', None)
            Week = request.POST.get('Week', None)
            employee =  request.POST.get('employee', None)

            data = {'Year': Year, 'Week': Week ,'employee':employee}
            rank = requests.post(remoteURL+"checktrackpro/api/Getemployeerankinfo",
                                data=data, headers=headers)
            if rank:
                return HttpResponse(json.dumps(rank.json()), content_type="application/json")
            else:
                return HttpResponse(json.dumps(rank.json()), content_type="application/json")
    else:
        return redirect('users:login')

@csrf_exempt
def publishrank(request):
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            Year = request.POST.get('Year', None)
            Week = request.POST.get('Week', None)
            data = {'Year': Year, 'Week': Week}
            rank = requests.post(remoteURL+"checktrackpro/api/rank",
                                data=data, headers=headers)
            if rank:
                return HttpResponse(json.dumps(rank.json()), content_type="application/json")
            else:
                return HttpResponse(json.dumps(rank.json()), content_type="application/json")
    else:
        return redirect('users:login')

def trackprocheckreport(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}

        w = datetime.datetime.now()
        currYear = w.year

        weekreqURL = remoteURL+'tasks/api/weekList?year={}'.format(currYear)
        weekExcludeResponse = requests.get(weekreqURL, headers=headers)
        weeksersponse = weekExcludeResponse.json()

        yeareqURL = remoteURL+'tasks/api/yearList'
        yearresp_ = requests.get(yeareqURL, headers=headers)
        yearsersponse = yearresp_.json()
          
        
        return render(request,'admin/trackproreport/trackprocheckreport.html',{'weeklist':weeksersponse,'yearlist':yearsersponse,'curryear':currYear})
    else:
        return redirect('users:login')
        
def trackprocheckreportdata(request):
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            Year = request.POST.get('Year')
            Week = request.POST.get('Week')
            data = {'Year': Year, 'Week': Week}
            result = requests.post(remoteURL+"checktrackpro/api/trackprocheck_report",
                                data=data, headers=headers)
            ranresp = result.json()
            return HttpResponse(json.dumps(ranresp), content_type="application/json")
    else:
        return redirect('users:login')
        

def reportfinalsubmit(request):
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            Year = request.POST.get('Year')
            Week = request.POST.get('Week')
            empid = request.POST.get('empid')
            data = {'Year': Year, 'Week': Week,'empid':empid}
            result = requests.post(remoteURL+"checktrackpro/api/reportfinalsubmitapi",
                                data=data, headers=headers)
            ranresp = result.json()
            return HttpResponse(json.dumps(ranresp), content_type="application/json")
    else:
        return redirect('users:login')
    
def getassignbytaskdata(request): 
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        data = {}
        if request.method == 'POST':
            data['taskid'] = request.POST.get('Taskid')
            gettaskurl = remoteURL+"checktrackpro/api/gettaskassignbymodal"
            editTaskResponse = requests.post(gettaskurl,data=data,headers=headers)
            taskresp = editTaskResponse.json()
        return HttpResponse(json.dumps(taskresp), content_type="application/json")
    else:
        return redirect('users:login')
    



def updatetaskassignby(request):
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        data = {}
        if request.method == 'POST':
            data['taskid'] = request.POST.get('Taskid')
            data['Taskassignby'] = request.POST.get('Taskassignby')

            gettaskurl = remoteURL+"checktrackpro/api/updateassignby"
            editTaskResponse = requests.post(gettaskurl,data=data,headers=headers)
            taskresp = editTaskResponse.json()
        return HttpResponse(json.dumps(taskresp), content_type="application/json")
    else:
        return redirect('users:login')
