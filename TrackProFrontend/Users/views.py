from django.shortcuts import render, redirect, HttpResponse,HttpResponseRedirect
import requests
import os
import json
from datetime import datetime,date,timedelta
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import datetime
from datetime import date
# from project.views import statuscheck
from leave.templatetags.encryption_filters import decrypt_parameter

remoteURL = "http://127.0.0.1:8000/"
frontendURL = 'http://127.0.0.1:8001/'

imageURL = remoteURL[:-1]

# from Users.context_processers import ImageURL as imageURL
leave_maped_managers_listurl=remoteURL+"leave/api/mapped_managers"
employee_filterurl=remoteURL+"users/api/employee_filter"
loginurl = remoteURL+"users/api/login"
logoutUrl = remoteURL + 'users/api/logout'
departmentUrl = remoteURL + "department/api/departmentlist"
userListUrl = remoteURL + "users/api/userlist"
userempListUrl = remoteURL + "users/api/user_emp_list"
getyearlydata_url=remoteURL+"leave/api/employee_yearly_total_days"
roleListUrl = remoteURL + 'users/api/rolelist'
addRoleUrl = remoteURL + 'users/api/addrole'
designationListUrl = remoteURL + 'users/api/designationlist'
addEmployeeUrl = remoteURL + 'users/api/adduser'
addDesignationUrl = remoteURL + 'users/api/adddesignation'
addLocationUrl = remoteURL + 'users/api/addlocation'
deleteLocationURL = remoteURL + "users/api/deletelocation"
locationListUrl = remoteURL + 'users/api/locationlist'
finYearListUrl = remoteURL + 'users/api/financialyearlist'
addFinYearUrl = remoteURL + 'users/api/addfinyear'
addMappingUrl = remoteURL + 'users/api/addmapping'
mappingListUrl = remoteURL + 'users/api/mappinglist'
ManagerUserListUrl = remoteURL + "users/api/ManagerUserListAPI"
permissionsListUrl = remoteURL + 'users/api/permissionlist'
MenuitemListUrl = remoteURL + 'users/api/menuitem'
updatepasswordURL = remoteURL + 'users/api/passwordupdate'
notificationlistURL = remoteURL + 'tasks/api/notificationlist'
readNotificationURL = remoteURL + 'tasks/api/readnotifications'
leaveNotificationURL = remoteURL + 'tasks/api/leavenotificationlist'
sendremindermailURL = remoteURL + 'company/api/sendactivereminder'
employeedetailURL = remoteURL + 'users/api/getuser'
employeeupdateURL = remoteURL + 'users/api/userupdate'
rolelistUrl = remoteURL + 'users/api/rolelist'
roleaddUrl = remoteURL + 'users/api/addrole'
updateroleURL = remoteURL + "users/api/updaterole"
locationlistURL = remoteURL + "users/api/locationlist"
addlocationURL = remoteURL + "users/api/addlocation"
updatelocationURL = remoteURL + "users/api/updatelocation"
desglistURL = remoteURL + "users/api/designationlist"
addDesgURL = remoteURL + "users/api/adddesignation"
updateDesgURL = remoteURL + "users/api/updatedesignation"
deleteDesgURL = remoteURL + "users/api/delete_designation"
deleteDepartURL= remoteURL + "department/api/deletedepartment"
addDepartmentURL = remoteURL + "department/api/addepartment"
updateDepartmentURL = remoteURL + "department/api/updatedepartment"
calendarUrl = remoteURL+"users/api/employee_calendar"
excellatemarkreporturl = remoteURL + 'leave/api/latemarkexcelreport'

forget_password_url = remoteURL+"users/api/chkemail"
reset_password_url = remoteURL+"users/api/resetpassword"
admindashboardURL = remoteURL+'users/api/admindashboarddata'
dashboardURL = remoteURL+'users/api/dashboarddata'
punch_inurl = remoteURL+"users/api/punch_indata"
punch_outurl = remoteURL+"users/api/punch_outdata"

punch_geturl = remoteURL+"users/api/punch_getdata"
announcementurl = remoteURL+"rules/announcementlist"
newsUrl = remoteURL+"rules/newslist"
locationurl = remoteURL+'users/api/locationcountdata'
permission_list_url = remoteURL+"users/api/rolepermissionlist"
menu_list_url = remoteURL+"users/api/menuitem"
role_list_url = remoteURL+"users/api/rolelist"
#added
fileDataUrl = remoteURL + 'users/api/newfiledata'
appendfileDataUrl = remoteURL + 'users/api/appendfiledata'
monthlydataurl = remoteURL + 'users/api/monthlydata'
attendanceList = remoteURL+"users/api/monthlydata"
weekperenturl =  remoteURL+"users/api/weeklypercentdata"
teamtrackerurl = remoteURL+"users/api/teamtrackerdataapi"
attstatisticsurl = remoteURL+"users/api/attstatisticsapi"
empbirthdayurl = remoteURL+"users/api/allempbdaydata"
todaystatusurl =  remoteURL+"users/api/admintodaysstatus_api"
rankcardurl = remoteURL+"users/api/rankcardapi"
addannouncementURL = remoteURL+"rules/addannouncement"
UpdateAnnouncementURL = remoteURL+"rules/updateannouncement"
deleteAnnouncementURL = remoteURL+"rules/deleteannouncement"
calendar_allUrl = remoteURL+"leave/api/getattendancecount"
delete_employee_url = remoteURL + "users/api/userblock"

onboardinglist_urls = remoteURL+"users/api/onboardinglist"
onboard_login_password_urls = remoteURL+"users/api/onboard_login_password"
acceptDocument_urls = remoteURL+"users/api/accept-document"
rejectedDocument_urls = remoteURL+"users/api/rejected-document"
addeducationaldetails_urls = remoteURL+"users/api/add_educational_details"
updatePersonalDetailsSecondaryInfo_urls = remoteURL+"users/api/update-personal-details-secondary-info"
updateEmployeDetailsSecondaryInfo_urls = remoteURL+"users/api/update-employe-details-secondary-info"
updateDetailsAndDocument_urls = remoteURL+"users/api/update-details-and-document"
secondaryInfoLinkApi_urls = remoteURL+"users/api/secondary-info-link"
get_late_mark_attendance_url = remoteURL + 'leave/api/get_late_mark_attendance'
get_late_mark_attendance_pagination_url= remoteURL + 'leave/api/pagination_get_late_mark_attendance'
#holiday
holidaylisturl =  remoteURL+"users/api/get_holidaylistdata"
dashboard_leave_cardurl = remoteURL + 'leave/api/dashboard_leave_card'
addholidayURL = remoteURL+"users/api/add_holidays"
UpdateholidayURL = remoteURL+"users/api/update_holidays"
deleteholidayURL = remoteURL+"users/api/delete_holidays"

#attrequest
atturl = remoteURL+"users/api/attendancerequestapi"
att_actionurl = remoteURL+"users/api/manageratt_request"
empattupdateurl = remoteURL+"users/api/Empl_attupdaterequest"
cancelrequesturl = remoteURL+"users/api/Empl_attcancelrequest"
sendwarningmailURL = remoteURL+"users/api/sendwarningmail"


tokenmsg = """<div style="font-family: 'Source Sans Pro','Helvetica Neue',Helvetica,Arial,sans-serif;">
            <h1>Session Expired</h1>
                <p>Click 
                    <a href="http://trackpro.oneroof.tech"> here</a>
                to login again</p>
            </div>
        """

def accessDenied(request):
    return render(request,'admin/errorPages/401.html')

def accessToPage(Menulist,url):
    response = {'Status':0,'Message':'NotPermissible'}
    for object in Menulist: 
        var =  str(object['MenuPath'])
        if var.strip() == url:
            response = {'Status':1,'Message':'Permissible'}
    if response['Status']== 1:
        return True
    else:
        return False
    
def statuscheck(statuscode):
    if statuscode != 200:        
        return True
    else:
        return False

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        desktopToken = request.POST['desktopToken']
        data = {}
        data['username'] = Username
        data['password'] = password
        data['desktopToken'] = desktopToken
        loginResponse = requests.post(loginurl, data=data)
        Response_ = loginResponse.json()
        if Response_.get('msg'):
            msg = Response_['msg']
            messages.error(request, msg)
            return render(request, 'login.html')
        if Response_.get('token'):
            token = Response_['token']
            request.session['token'] = token  
        if Response_.get('userRoleID'):
            userRoleID = Response_['userRoleID']
            request.session['userRoleID'] = userRoleID
        if Response_.get('user'):
            userIDresponse = Response_['user']
            FirstnameAPIresponse = Response_['Firstname']
            LastnameAPIresponse = Response_['Lastname']
            Designationresponse = Response_['Designation']
            userprfileresponse = Response_['userprofile']

            Menu = Response_['Menu']

            request.session['Firstname'] = FirstnameAPIresponse
            request.session['Lastname'] = LastnameAPIresponse
            request.session['Designation'] = Designationresponse
            request.session['Menu'] = Menu
            request.session['userID'] = userIDresponse
            request.session['userPhoto'] = userprfileresponse
            request.session['PasswordChanged'] = Response_.get(
                'PasswordChanged')
            request.session['email'] = Response_.get('email')
            request.session['secondary_info'] = Response_.get('secondary_info')
            request.session['company_code'] = Response_.get('company_code')
            request.session['superadmin'] = Response_.get('superadmin')
            request.session['typeofwork'] = Response_.get('typeofwork')
            request.session['employeeId'] = Response_.get('employeeId')
            request.session['present'] = Response_.get('present')
            request.session['is_staff'] = Response_.get('is_staff')
            request.session['userEmployeeId'] = Response_.get('employeeId')
            request.session['rules'] = Response_.get('rules')
            request.session['companylogo'] = Response_.get('companyimage')
            request.session['rolename'] = Response_.get('rolename')

        if Response_.get('Roleid'):
            Role = Response_['Roleid']
            request.session['roleID'] = Role

        if Response_['n'] == 1:
            if Response_['superadmin'] == True:
                return redirect('users:home')
            else:
                if Response_['is_staff'] == False and Response_['masters'] == False:
                    return redirect('company:companyrule')
                if Response_['is_staff'] == False and Response_['rules'] == False:
                    return redirect('company:companywarmanagement')
                # if Response_['secondary_info'] == False:
                #     return redirect('users:secondary_info')
                else:
                    return redirect('users:dashboard')
        else:
            messages.error(request, Response_['msg'])
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')



def logout(request):
    try:
        tok = request.session.get('token', False)
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        logoutUrl = remoteURL+'users/api/logout'
        logoutResponse = requests.post(logoutUrl, headers=headers)
        Response_ = logoutResponse.json()
        if Response_.get('n') == 1:
            del request.session['token']
            return redirect('users:login')
        else:
            return redirect('users:login') # change this.
    except Exception as e:
        return HttpResponse('logout failed')

def home(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    Menu = request.session['Menu']
    url = request.path
    access = accessToPage(Menu, url)
    if access == False:
        return redirect('users:accessDenied')
    if tok:
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        notificationlistResponse = requests.get(notificationlistURL, headers=headers)
        if notificationlistResponse.status_code != 200:
            messages.error(request,'Session expired !')
            return redirect ('users:login')
        notResponse_ = notificationlistResponse.json()


        CompanyadmindataURL = remoteURL+"company/api/companycountdashboard"
        companydata = requests.get(CompanyadmindataURL, headers=headers)
        companyResponse_ = companydata.json()


        w = datetime.datetime.now()
        currYear = w.year

        BillingPeriodlistUrl = remoteURL + 'company/api/billingPeriodlist'
        periodlistResponse = requests.get(BillingPeriodlistUrl, headers=headers)
        periodlistData = periodlistResponse.json()


        return render(request, 'superadmin/dashboard.html',{
            # 'notificationlist':notResponse_['data'],
            'notificationCount':notResponse_['notificationCount'],
            'planlist':periodlistData['data'],
            'countdata':companyResponse_['data'],
            'currentyear':currYear})
    else:
        return redirect('users:login')    

def testhome(request):
    return render(request, 'superadmin/test.html')

def updatepassword(request,id):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        staff =request.session.get('is_staff')
        superadmin = request.session.get('superadmin')
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data = {}
        if request.method == 'GET':
            if superadmin == True :
                return render(request, 'admin/masters/changepassword.html')
            else:
                return render(request, 'admin/masters/changepassword.html')
        else:
            data['email'] = request.session.get('email')
            data['password'] = request.POST.get('newpassword')
            data['oldpassword'] = request.POST.get('oldpassword')
            updatePasswordStrUrl = updatepasswordURL + "?userID=" + str(id)
            updatepasswordResponse = requests.post(updatePasswordStrUrl, headers=headers,data=data)
            Response_ = updatepasswordResponse.json()
            if Response_['n'] == 1:
                messages.success(request, Response_['Msg'])
                return redirect('users:login')
            else:
                messages.warning(request, Response_['Msg'])
                return render(request, 'admin/masters/changepassword.html')
    else:
        return redirect('users:login')     

def readNotification(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        readNotificationResponse = requests.get(readNotificationURL, headers=headers)
        readNotificationData = readNotificationResponse.json()
        return HttpResponse(json.dumps({'data': readNotificationData}), content_type="application/json")
    else:
        return redirect('users:login')    

def leavenotificationlist(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        leaveNotificationResponse = requests.get(leaveNotificationURL, headers=headers)
        leaveNotificationData = leaveNotificationResponse.json()
        return HttpResponse(json.dumps({'data': leaveNotificationData}), content_type="application/json")
    else:
        return redirect('users:login')   

def notificationlist(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        notificationlistResponse = requests.get(notificationlistURL, headers=headers)
        notResponse_ = notificationlistResponse.json()   
        return HttpResponse(json.dumps({'count':notResponse_['notificationCount'],'leavecount':notResponse_['pendingleaveobj'],'trackprocheckcount':notResponse_['trackprocheckcount']}), content_type="application/json")
    else:
        return redirect('users:login')     
    
def sendActiveREminderMail(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        sendremindermailResponse = requests.get(sendremindermailURL, headers=headers)
        sendResponse_ = sendremindermailResponse.json()
        return HttpResponse(json.dumps({'data': sendResponse_}), content_type="application/json")
    else:
        return redirect('users:login')
#ADMIN
    
def getfullname(request):
    Firstname = request.session['Firstname']
    Lastname = request.session['Lastname']
    Fullname = Firstname + ' ' + Lastname
    return Fullname

def admindashboard(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok is not None:
        is_staff = request.session.get('is_staff')
        adminrole = (request.session.get('rolename')).lower()
        today = date.today()
        weeks = []
        year, week, _ = today.isocalendar()
        currentweek = week
        for i in range(1,currentweek):
            # Subtract a week from the initial 'today'
            today -= timedelta(weeks=1)

            # This handles some formatting to make it consistent with expected output:
            year, week, _ = today.isocalendar()
            weeks.append({
                "weekname":"Week "+ "{0:02d}".format(week),
                "no":week
                })
            
        typeofwork = request.session.get('typeofwork')
        employeeId = request.session.get('employeeId')
        present = request.session.get('present')
        UserId = request.session['userID']
        # getCurrUserdata = userforpage(request)
        if request.session.get('PasswordChanged') == False:
            return redirect('updatepassword/{}'.format(request.session.get('userID')))
        if tok:
            tok = request.session['token']
            t = 'Token {}'.format(tok)
            headers = {'Authorization': t}
            UserId = request.session['userID']

            # get Menu
            Menu = request.session['Menu']
            url = request.path
            access = accessToPage(Menu, url)
            if access == False:
                return redirect('users:accessDenied')
            
            Fullname = getfullname(request)
            data = {'userID': UserId}
            birthDayDict = ""

            getUserUrl = remoteURL + 'users/api/getuser?userID={}'.format(UserId)
            usersResponse = requests.get(getUserUrl, headers=headers)

            if usersResponse.status_code != 200:
                messages.error(request,'Session expired !')
                return redirect ('users:login')

            userInfo = usersResponse.json()
            birthDay = userInfo['data']['BirthDate'].split("-")
            employeeBday = birthDay[1] + "-" +birthDay[2]
            currentDate = date.today()
            currentDaySplit = str(currentDate).split("-")
            currentDay = currentDaySplit[1] + "-" + currentDaySplit[2]
            if currentDay == employeeBday:
                birthDayDict = True
            else:
                birthDayDict = False

            dashboardResponse = requests.post(
                admindashboardURL, data=data, headers=headers)
            dashboard = dashboardResponse.json()

            all_dept_graph_data = dashboard['data']['all_dept_graph_data']
            all_dept_weeklist = dashboard['data']['all_dept_weeklist']
            last_task = dashboard['data']['lasttask']


            locationResponse = requests.get(
                locationurl, headers=headers)
            location = locationResponse.json()
            locationdata = location['data']

            month = date.today().month
            bdResponse = requests.get(
                empbirthdayurl, headers=headers)
            allbdayann = bdResponse.json()
            allbirthdaydata = allbdayann['data']['birthdaylist']
            allannouncementdata = allbdayann['data']['announcementlist']
            Monthlist = [{'month':1,'monthname':'January'},
                        {'month':2,'monthname':'February'},
                        {'month':3,'monthname':'March'},
                        {'month':4,'monthname':'April'},
                        {'month':5,'monthname':'May'},
                        {'month':6,'monthname':'June'},
                        {'month':7,'monthname':'July'},
                        {'month':8,'monthname':'August'},
                        {'month':9,'monthname':'September'},
                        {'month':10,'monthname':'October'},
                        {'month':11,'monthname':'November'},
                        {'month':12,'monthname':'December'}]


            Todaysstatus = requests.get(
            todaystatusurl,data=data, headers=headers)
            Todaysstatus_res = Todaysstatus.json()
            todaystatus_list = Todaysstatus_res['data']

            w = datetime.datetime.now()
            currYear = w.year
            weekreqURL = remoteURL+'tasks/api/weekList?year={}'.format(currYear)
            weekExcludeResponse = requests.get(weekreqURL, headers=headers)
            weeksersponse = weekExcludeResponse.json()
            my_date = datetime.date.today()
            year, week_num, day_of_week = my_date.isocalendar()
            currweek = week_num
            prevweek = currweek-1
        
            # data = announcementdata + newsdata
            if all_dept_graph_data == []:
                all_dept_graph_data_key = []
            else:
                all_dept_graph_data_key =  all_dept_graph_data.items()
            return render(request, 'admin/admindashboard.html', {'Fullname': Fullname,
                                                        'Menu': Menu, 'getCurrUserdata': "getCurrUserdata",
                                                        'dashboard': dashboard, 'userID': UserId,
                                                        'all_dept_weeklist': all_dept_weeklist,
                                                        'all_dept_graph_data': json.dumps(all_dept_graph_data),
                                                        'dept_graph_legend': all_dept_graph_data_key,
                                                        'last_task':last_task,
                                                        'locationcountdata':locationdata,
                                                        'allbdaylist':allbirthdaydata,
                                                        'announcements':allannouncementdata,
                                                        'typeofwork':typeofwork , 'employeeId':employeeId, 'present':present,"birthDayDict":birthDayDict,
                                                        "Monthlist":Monthlist,"currentmonth":month,'prevweek':prevweek,'weeklist':weeksersponse,
                                                        "weeklist":weeks,'todaystatus_list':todaystatus_list
                                                        })
        else:
            return redirect('users:login')
    else:
        return redirect('users:login')



def adminhome(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token')
    if tok is not None:
        is_staff = request.session.get('is_staff')
        today = date.today()
        weeks = []
        year, week, _ = today.isocalendar()
        currentweek = week
        for i in range(1,currentweek):
            # Subtract a week from the initial 'today'
            today -= timedelta(weeks=1)

            # This handles some formatting to make it consistent with expected output:
            year, week, _ = today.isocalendar()
            weeks.append({
                "weekname":"Week "+ "{0:02d}".format(week),
                "no":week
                })
            
        if is_staff == True:
            tok = request.session.get('token', False)
            UserId = request.session['userID']
            if request.session.get('PasswordChanged') == False:
                return redirect('updatepassword/{}'.format(request.session.get('userID')))
            if tok:
                tok = request.session['token']  
                
                t = 'Token {}'.format(tok)
                headers = {'Authorization': t}
                UserId = request.session['userID']

                # get Menu
                Menu = request.session['Menu']
                url = request.path
                access = accessToPage(Menu, url)
                if access == False:
                    return redirect('users:accessDenied')
                
                data = {'userID': UserId}
               


                checkindataurl = remoteURL + 'users/api/usercheckininfo'
                checkinResponse = requests.get(checkindataurl, headers=headers)
                if checkinResponse.status_code != 200:
                    messages.error(request,'Session expired !')
                    return redirect ('users:login')
                checkinInfo = checkinResponse.json()

                
                weeklypercentResponse =  requests.post(
                weekperenturl,data=data, headers=headers)
                WeeklyPercentres = weeklypercentResponse.json()
                
                
                attstatistics = requests.get(
                attstatisticsurl, headers=headers)
                attresponse = attstatistics.json()
                
                
                
                bdResponse = requests.get(
                    empbirthdayurl, headers=headers)
                allbdayann = bdResponse.json()
                
                dashboardResponse = requests.post(
                    admindashboardURL, data=data, headers=headers)
                dashboard = dashboardResponse.json()
                
                
                # allow_web_checkin_request = requests.post(allow_web_checkin_url, data=data, headers=headers)
                # allow_web_checkin_response = allow_web_checkin_request.json()
                
                
                
                
                return render(request, 'admin/staffdashboard.html', {
                                                                'checkinstatus':checkinInfo['data']['checkinallowed'] ,
                                                                "requestbtn":checkinInfo['data']['requestbtn'],
                                                                'allbdaylist':allbdayann['data']['birthdaylist'],
                                                                'announcements':allbdayann['data']['announcementlist'],
                                                                'taskthisweek':dashboard['data']['Tasks'],
                                                                'totaltasks':dashboard['data']['TotalTask'],
                                                                'last_task': dashboard['data']['lasttask'],
                                                                "rankcard_data":dashboard['data']['userprevweekdata'],
                                                                'weeklypercentdata':WeeklyPercentres['data'],
                                                                'attendancegraphdata':attresponse['data'],
                                                                # 'allow_web_checkin'
                                                            })
        else:
            
            tok = request.session.get('token', False)


            if request.session.get('PasswordChanged') == False:
                return redirect('updatepassword/{}'.format(request.session.get('userID')))
            if tok:
                tok = request.session['token']
                t = 'Token {}'.format(tok)
                headers = {'Authorization': t}
                UserId = request.session['userID']

                # get Menu
                Menu = request.session['Menu']
                url = request.path
                access = accessToPage(Menu, url)
                if access == False:
                    return redirect('users:accessDenied')
                
                data = {'userID': UserId}

                locationResponse = requests.get(
                    locationurl, headers=headers)
                if locationResponse.status_code != 200:
                    messages.error(request,'Session expired !')
                    return redirect ('users:login')
                location = locationResponse.json()

                locationdata = location['data']

                #all emp birthdays and announcements
                bdResponse = requests.get(
                    empbirthdayurl, headers=headers)
                allbdayann = bdResponse.json()

                allbirthdaydata = allbdayann['data']['birthdaylist']
                allannouncementdata = allbdayann['data']['announcementlist']
                Monthlist = [{'month':1,'monthname':'January'},
                            {'month':2,'monthname':'February'},
                            {'month':3,'monthname':'March'},
                            {'month':4,'monthname':'April'},
                            {'month':5,'monthname':'May'},
                            {'month':6,'monthname':'June'},
                            {'month':7,'monthname':'July'},
                            {'month':8,'monthname':'August'},
                            {'month':9,'monthname':'September'},
                            {'month':10,'monthname':'October'},
                            {'month':11,'monthname':'November'},
                            {'month':12,'monthname':'December'}]


                month = date.today().month
                my_date = datetime.date.today()
                year, week_num, day_of_week = my_date.isocalendar()
                currweek = week_num
                prevweek = currweek-1
                Todaysstatus = requests.get(
                todaystatusurl,data=data, headers=headers)
                Todaysstatus_res = Todaysstatus.json()
                todaystatus_list = Todaysstatus_res['data']
    
                
                return render(request, 'admin/admindashboard.html', {
                                                            'locationcountdata':locationdata,
                                                            'allbdaylist':allbirthdaydata,
                                                            'announcements':allannouncementdata,
                                                            "Monthlist":Monthlist,
                                                            "currentmonth":month,
                                                            'prevweek':prevweek,
                                                            "weeklist":weeks,
                                                            'todaystatus_list':todaystatus_list
                                                            })
    else:
        return redirect('users:login')



def employeelist(request):

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

        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "GET":
            empListUrl = remoteURL + "users/api/employee_master_emp_list"

            employeelistResponse = requests.get(empListUrl, headers=headers)
            employeelistData = employeelistResponse.json()

            
            typeofworkdata = [{'id':"1",'type':'Work From Home'},{'id':"2",'type':'Work From Office'},{'id':"3",'type':'Outdoor'},{'id':"4",'type':'Hybrid'}]
            return render(request, 'admin/employeemaster/employeelist.html',{
                    'employeelist':employeelistData['data'],

                    'typelist':typeofworkdata
                  })
    else:
        return redirect('users:login')  

def addemployee(request):
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
            deptlistResp = requests.get(departmentUrl, headers=headers)
            deptlistData = deptlistResp.json()
            designatiolistResponse = requests.get(designationListUrl, headers=headers)
            desglistData = designatiolistResponse.json()
            locationlistResponse = requests.get(locationListUrl, headers=headers)
            locationData = locationlistResponse.json()
            rolelistResponse = requests.get(roleListUrl,headers=headers)
            roleData = rolelistResponse.json()
            typeofworkdata = [{'id':"1",'type':'Work From Home'},{'id':"2",'type':'Work From Office'},{'id':"3",'type':'Outdoor'},{'id':"4",'type':'Hybrid'}]
            employeestatusdata = [{'statusvalue':'probation','statusName':'Probation'},{'statusvalue':'confirm','statusName':'Confirm'},{'statusvalue':'trainee','statusName':'Trainee'},{'statusvalue':'intern','statusName':'Intern'}]
    
            return render(request,'admin/employeemaster/addemployee.html',{'designationlist':desglistData['data'],'deptlist':deptlistData['data'],'locationlist':locationData['data'],'rolelist':roleData['data'],'typelist':typeofworkdata,'statuslist':employeestatusdata})
        else:
            data = {}
            # fullname = request.POST.get('fullname')
            doj = request.POST.get('DateofJoining')
            splitDoj = doj.split('-')
            dojstr = '-'.join(reversed(splitDoj))
            dob=request.POST.get('DateofBirth')
            dobstr=''
            if dob is not None and dob !='':
                splitDoj = dob.split('-')
                dobstr = '-'.join(reversed(splitDoj))
            data['Firstname'] =  request.POST.get('firstname')
            data['Lastname'] =  request.POST.get('lastname')

            data['email'] = request.POST.get('email')
            data['DateofJoining'] = dojstr
            data['BirthDate'] = dobstr
            data['DesignationId'] = request.POST.get('designation')
            data['RoleID'] = request.POST.get('role')
            data['employeetype'] = request.POST.get('employeetype')
            data['DepartmentID'] = request.POST.getlist('DepartmentID')
            data['locationId'] = request.POST.get('location')
            data['Phone'] = request.POST.get('MobileNumber')
            data['typeofwork'] = request.POST.get('typeofwork')
            data['employeeId'] = request.POST.get('employeeId')
            data['employeementStatus'] = request.POST.get('employeeStatus')
            data['personal_email'] = request.POST.get('personal_email')
            data['password'] = request.POST.get('password')

            addEmpResponse = requests.post(addEmployeeUrl,headers=headers,data=data)
            addEmpData = addEmpResponse.json()
            if addEmpData['n'] == 1:
                messages.success(request,addEmpData['Msg'])
                return redirect ('users:employeelist')
            else:
                messages.error(request,addEmpData['Msg'])
                return redirect ('users:employeelist')

    else:
        return redirect('users:login')

def update_employee(request,id):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        id=int(decrypt_parameter(id))
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "GET":

            Employee_all_info_by_idURL = remoteURL + 'users/api/Employee_all_info_by_id'
            data={}
            data['userid']=id
            employeebyiddata = requests.post(Employee_all_info_by_idURL,data=data,headers=headers) 
            employeeiddata = employeebyiddata.json()
            ssc_qualification = next((q for q in employeeiddata['data']['educationdetails'] if q['qualification_name'] == 'SSC'), None)

            HSC_qualification = next((q for q in employeeiddata['data']['educationdetails'] if q['qualification_name'] == 'HSC'), None)

            gaduation = next((q for q in employeeiddata['data']['educationdetails'] if q['qualification_name'] == 'Graduation/Degree'), None)

            POSTGraduation = next((q for q in employeeiddata['data']['educationdetails'] if q['qualification_name'] == 'POST Graduation'), None)







            
            context={
                        'employeedetails':employeeiddata['data'],
                        'hostUrl':imageURL,
                        'userID':id,
                        "ssc_qualification":ssc_qualification,
                        "HSC_qualification":HSC_qualification,
                        "POSTGraduation":POSTGraduation,
                        "gaduation":gaduation,


                        
                    }


            # context={}
            # return render(request, 'admin/employeemaster/updateemployee.html',context)
            return render(request, 'admin/employeemaster/update_multiple_employees.html',context)
        else:
            data = {}
            doj = request.POST.get('DateofJoining')
            splitDoj = doj.split('-')
            if len(splitDoj[0]) > 3 :
                data['DateofJoining'] = request.POST.get('DateofJoining')
            else:
                dojstr = '-'.join(reversed(splitDoj))
                data['DateofJoining'] = dojstr

            dob = request.POST.get('DateofBirth')
            splitDob = dob.split('-')
            if len(splitDob[0]) > 3 :
                data['BirthDate'] = request.POST.get('DateofBirth')
            else:
                dobstr = '-'.join(reversed(splitDob))
                data['BirthDate'] = dobstr
                
            data['Firstname']=  request.POST.get('firstname')
            data['Lastname']=  request.POST.get('lastname')
            data['password'] = request.POST.get('password')
            data['email'] = request.POST.get('email')
            data['DesignationId'] = request.POST.get('designation')
            data['RoleID'] = request.POST.get('role')
            data['DepartmentID'] = request.POST.getlist('DepartmentID')
            data['locationId'] = request.POST.get('location')
            data['Phone'] = request.POST.get('MobileNumber')
            data['typeofwork'] = request.POST.get('typeofwork')
            data['employeeId'] = request.POST.get('employeeId')
            data['employeementStatus'] = request.POST.get('employeeStatus')
            strupdateUserURL = employeeupdateURL + "?userID=" + str(id)
            addEmpResponse = requests.post(strupdateUserURL,headers=headers,data=data)
            addEmpData = addEmpResponse.json()
            if addEmpData['n'] == 1:
                messages.success(request,addEmpData['Msg'])
                return redirect ('users:employeelist')
            else:
                messages.error(request,addEmpData['Msg'])
                return redirect ('users:employeelist')

    else:
        return redirect('users:login')
    
def block_employee(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "GET":
            data ={}
            data['userID'] = id
            delete_employee_request = requests.get(delete_employee_url,data=data,headers=headers)
            delete_employee_response = delete_employee_request.json()
            if delete_employee_response['n'] == 1:
                messages.success(request,delete_employee_response['Msg'])
                return redirect ('users:employeelist')
            else:
                messages.error(request,delete_employee_response['Msg'])
                return redirect ('users:employeelist')
        else:
            return redirect ('users:employeelist')
    else:
        return redirect('users:login')
        
        
        
def block_employee_ajax(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "POST":
            data ={}
            data['userID'] = request.POST.get('id')
            delete_employee_request = requests.get(delete_employee_url,data=data,headers=headers)
            delete_employee_response = delete_employee_request.json()
            return HttpResponse(json.dumps(delete_employee_response), content_type="application/json")
        else:
            return HttpResponse(json.dumps( {'n': 0, 'Msg': 'method not allowed', 'Status': 'error'}), content_type="application/json")
    else:
        return HttpResponse(json.dumps( {'n': 0, 'Msg': 'please login again', 'Status': 'error'}), content_type="application/json")
        
        
def rolelist(request):
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
            rolelistreponse = requests.get(rolelistUrl,headers=headers)   
            roledata = rolelistreponse.json()
            return render(request, 'admin/companyrolemaster/role.html',{'rolelist':roledata['data']})
        else:
            data = {}
            data['RoleName'] = request.POST.get('RoleName')
            roleaddreponse = requests.post(roleaddUrl,headers=headers,data=data)   
            roledata = roleaddreponse.json()
            if roledata['n'] == 1:
                messages.success(request,roledata['Msg'])
                return redirect ('users:rolelist')
            else:
                messages.error(request,roledata['Msg'])
                return redirect ('users:rolelist') 
    else:
        return redirect('users:login')
    
def locationlist(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "GET":
            if checksession(request):
                messages.error(request,'Session expired !')
                return redirect ('users:login') 

            locationlistreponse = requests.get(locationlistURL,headers=headers)

            # if locationlistreponse.status_code != 200:
            #     messages.error(request,'Session expired !')
            #     return redirect ('users:login') 
            
            locationdata = locationlistreponse.json()
            return render(request, 'admin/masters/location.html',{'locationlist':locationdata['data']})
        else:
            data = {}
            data['LocationName'] = request.POST.get('LocationName')
            data['lattitude'] = request.POST.get('lattitude')
            data['longitude'] = request.POST.get('longitude')
            data['meter'] = request.POST.get('meter')
            data['address'] = request.POST.get('address')
            


            addlocationreponse = requests.post(addlocationURL,headers=headers,data=data)   
            addlocationdata = addlocationreponse.json()
            if addlocationdata['n'] == 1:
                messages.success(request,addlocationdata['Msg'])
                return redirect ('users:locationlist')
            else:
                messages.error(request,addlocationdata['Msg'])
                return redirect ('users:locationlist') 
    else:
        return redirect('users:login')

def updateLocation(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data ={}
        locationId = request.POST.get('locationId')
        data ['LocationName'] = request.POST.get('LocationName')
        data['lattitude'] = request.POST.get('lattitude')
        data['longitude'] = request.POST.get('longitude')
        data['meter'] = request.POST.get('meter')
        data['address'] = request.POST.get('address')
        updateLocationStringUrl = updatelocationURL + "?locationID=" + str(locationId)
        updateLocationResponse = requests.post(updateLocationStringUrl, headers=headers,data=data)
        updateLocationData = updateLocationResponse.json()
        if updateLocationData['n'] == 1 :
            messages.success(request,updateLocationData['Msg'])
        else:
            messages.error(request,updateLocationData['Msg'])
        return HttpResponse(json.dumps({'data': updateLocationData}), content_type="application/json")
    else:
        return redirect('users:login')

def designationlist(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "GET":
            desglistreponse = requests.get(desglistURL,headers=headers) 
            if desglistreponse.status_code != 200:
                messages.error(request,'Session expired !')
                return redirect ('users:login')   
            desgdata = desglistreponse.json()
            return render(request, 'admin/masters/designation.html',{'designationlist':desgdata['data']})
        else:
            data = {}
            data['DesignationName'] = request.POST.get('DesignationName')
            adddesgreponse = requests.post(addDesgURL,headers=headers,data=data)   
            adddesgdata = adddesgreponse.json()
            if adddesgdata['n'] == 1:
                messages.success(request,adddesgdata['Msg'])
                return redirect ('users:designationlist')
            else:
                messages.error(request,adddesgdata['Msg'])
                return redirect ('users:designationlist') 
    else:
        return redirect('users:login')

def updatedesignation(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data ={}
        designationId = request.POST.get('designationId')
        data ['DesignationName'] = request.POST.get('DesignationName')
        updateDesignationStringUrl = updateDesgURL + "?designationID=" + str(designationId)
        updateDesignationResponse = requests.post(updateDesignationStringUrl, headers=headers,data=data)
        updateDesignationData = updateDesignationResponse.json()
        if updateDesignationData['n'] == 1 :
            messages.success(request,updateDesignationData['Msg'])
        else:
            messages.error(request,updateDesignationData['Msg'])
        return HttpResponse(json.dumps({'data': updateDesignationData}), content_type="application/json")
    else:
        return redirect('users:login')

def departmentlist(request):
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
            deptlistreponse = requests.get(departmentUrl,headers=headers)   
            deptdata = deptlistreponse.json()

            employeelistResponse = requests.get(userListUrl, headers=headers)
            employeelistData = employeelistResponse.json()

            return render(request, 'admin/masters/department.html',{'departmentlist':deptdata['data'],'employeelist':employeelistData['data']})
        else:
            data = {}
            data['DepartmentName'] = request.POST.get('DepartmentName')
            data['DepartmentHead'] = request.POST.get('departmenthead')

            adddeptreponse = requests.post(addDepartmentURL,headers=headers,data=data)   
            adddeptdata = adddeptreponse.json()
            if adddeptdata['n'] == 1:
                messages.success(request,adddeptdata['Msg'])
                return redirect ('users:departmentlist')
            else:
                messages.error(request,adddeptdata['Msg'])
                return redirect ('users:departmentlist') 
    else:
        return redirect('users:login')

def updatedepartment(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data ={}
        departmentId = request.POST.get('departmentId')
        data ['DepartmentName'] = request.POST.get('DepartmentName')
        data ['DepartmentHead'] = request.POST.get('departmenthead')
        updateDeptStringUrl = updateDepartmentURL + "?departmentID=" + str(departmentId)
        updateDeptResponse = requests.post(updateDeptStringUrl, headers=headers,data=data)
        updateDeptData = updateDeptResponse.json()
        if updateDeptData['n'] == 1 :
            messages.success(request,updateDeptData['Msg'])
        else:
            messages.error(request,updateDeptData['Msg'])
        return HttpResponse(json.dumps({'data': updateDeptData}), content_type="application/json")
    else:
            return redirect('users:login')

def addusermanagermapping(request):
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
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "GET":
            employeelistResponse = requests.get(userListUrl, headers=headers)
            employeelistData = employeelistResponse.json()
            mappinglistResponse = requests.get(ManagerUserListUrl, headers=headers)
            mappinglistData = mappinglistResponse.json()
            return render(request, 'admin/masters/usermanagermapping.html',{'employeelist':employeelistData['data'],'mappinglist':mappinglistData['data']})
        else:
            data = {}
            data['ManagerID'] = request.POST.get('ManagerID')
            data['UserID'] = request.POST.getlist('UserID')
            addmappingResponse = requests.post(addMappingUrl, data=data, headers=headers)
            Response_ = addmappingResponse.json()
            if Response_['n'] == 1:
                messages.success(request,Response_['Msg'])
                return redirect ('users:addusermanagermapping')
            else:
                messages.error(request,Response_['Msg'])
                return redirect ('users:addusermanagermapping') 
    else:
        return redirect('users:login')



def deleteusermappings(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}
            data['ManagerID'] = request.POST.get('ManagerID')
            deleteusermappingsurl = remoteURL+'users/api/deleteMapping'
            Response_ = requests.post(deleteusermappingsurl, data=data, headers=headers)
            response_data = Response_.json()
            return HttpResponse(json.dumps(response_data),content_type='application/json')
    else:
        return redirect('users:login')


@csrf_exempt
def MappingSelectOnchangeAjax(request):
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            Managerid = request.POST.get('id', None)

            updateMappingUrl = remoteURL + \
                'users/api/mappingJoinQuery?ManagerID={}'.format(Managerid)
            Mapp = requests.get(updateMappingUrl, headers=headers)
            if Mapp:
                mappings = Mapp.json()
                return HttpResponse(json.dumps(mappings), content_type="application/json")
            else:
                return HttpResponse(json.dumps({'n': 0, 'Msg': 'Json object not serialized', 'Status': 'Failed'}), content_type="application/json")
    else:
        return redirect('users:login')

def war_report(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        employee_list=requests.get(userListUrl, headers=headers)
        employee_list_response = employee_list.json()
        return render(request,'admin/trackproreport/trackproreport.html',{'employeelist':employee_list_response['data']})
    else:
        return redirect('users:login')
    
def emplist(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            data={}
            data['username']=request.POST.get('username')
            employeelisturl = remoteURL + "users/api/search_by_name_employee"

            request_ = requests.post(employeelisturl,data=data,headers=headers)
            response_data = request_.json()
            
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return HttpResponse({'n': 0,'msg':"Method not allowed"}, content_type="application/json")
    else:
        return HttpResponse({'n': 0,'msg':"login required"}, content_type="application/json")    

def getuserlist(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'GET':

            request_ = requests.get(userListUrl,headers=headers)
            response_data = request_.json()
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return HttpResponse({'n': 0,'msg':"Method not allowed"}, content_type="application/json")
    else:
        return HttpResponse({'n': 0,'msg':"login required"}, content_type="application/json")    

def get_emp_by_id(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            data={}
            data['managerid']=request.POST.get('managerid')
            employeedataurl = remoteURL + "users/api/search_emp_by_id"

            request_ = requests.post(employeedataurl,data=data,headers=headers)
            response_data = request_.json()
            
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return HttpResponse({'n': 0,'msg':"Method not allowed"}, content_type="application/json")
    else:
        return HttpResponse({'n': 0,'msg':"login required"}, content_type="application/json")    

def late_attendance(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}

        if request.method =="POST":
            data['start_date'] = request.POST.get("start_date")
            data['end_date'] = request.POST.get("end_date")
            data['empId'] = request.POST.get("empId")
            p= request.POST.get('p')
            get_pagination_request_url = get_late_mark_attendance_pagination_url + "?p=" +str(p)
            get_pagination_request=requests.post(get_pagination_request_url,data=data,headers=headers)
            get_pagination_response=get_pagination_request.json()
            return HttpResponse(json.dumps(get_pagination_response),content_type='application/json')
        userlist = requests.get(userListUrl,headers=headers)
        userresponse = userlist.json()

        return render(request,'admin/Attendance/late_attendance.html',{'employees':userresponse['data']})
    else:
        return redirect('users:login')
     
@csrf_exempt
def attendance_cal(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        adminrole = (request.session.get('rolename')).lower()
        headers = {'Authorization': t}
        today = datetime.date.today()
        if checksession(request):
            messages.error(request,'Session expired !')
            return redirect ('users:login') 
        if adminrole == "admin" or adminrole == "core team":

            data={}
            data['year'] = today.year
            data['month'] = today.month
            data['UserId'] = request.session['userID']
            userid = request.session['userID']
            firstname = request.session['Firstname']
            lastname = request.session['Lastname']
            username= firstname + ' ' + lastname

            if request.method == 'POST':
                data['month'] = request.POST.get('month')
                data['year'] = request.POST.get('year')
                data['UserId'] = request.POST.get('empid')
                if data['UserId'] == "All":

                    calendar_allUrl = remoteURL+"leave/api/getattendancecount"
                    response1 = requests.post(calendar_allUrl,data=data,headers=headers)
                    caldata = response1.json()
                    
                else:

                    response1 = requests.post(calendarUrl,data=data,headers=headers)
                    caldata = response1.json()
                return HttpResponse(json.dumps(caldata),content_type='application/json')
            
            
            
            managermapedlist = requests.get(leave_maped_managers_listurl,headers=headers)
            maped_managers = managermapedlist.json()

            todaysdate = date.today()
            currentmonth = todaysdate.month
            currentyear = todaysdate.year

            context={       
                        "CoreTeam":True,
                        "managerlist":maped_managers['data'],
                        "currentmonth":currentmonth,
                        "currentyear":currentyear,
                        "UserId" : userid,
                        "username":username,
                    }
            
            return render(request,'admin/Attendance/adminattendance_calendar.html',context
                        )

        else:

            data={}
            data['year'] = today.year
            data['month'] = today.month
            data['UserId'] = request.session['userID']
            userid = request.session['userID']
            firstname = request.session['Firstname']
            lastname = request.session['Lastname']
            username= firstname + ' ' + lastname

            if request.method == 'POST':
                data['month'] = request.POST.get('month')
                data['year'] = request.POST.get('year')
                data['UserId'] = request.POST.get('empid')
                if data['UserId'] == "All":
                    calendar_allUrl = remoteURL+"leave/api/getattendancecount?userid={}".format(userid)
                    response1 = requests.post(calendar_allUrl,data=data,headers=headers)
                    caldata = response1.json()
                else:
                    response1 = requests.post(calendarUrl,data=data,headers=headers)
                    caldata = response1.json()
                return HttpResponse(json.dumps(caldata),content_type='application/json')
            
            
            managermapedlist = requests.get(leave_maped_managers_listurl,headers=headers)
            maped_managers = managermapedlist.json()

            todaysdate = date.today()
            currentmonth = todaysdate.month
            currentyear = todaysdate.year
            return render(request,'admin/Attendance/adminattendance_calendar.html',
                        {
                                "CoreTeam":False,
                                "managerlist":maped_managers['data'],
                                "currentmonth":currentmonth,
                                "currentyear":currentyear,
                                "UserId" : userid,
                                "username":username,
                            })
    else:
        return redirect('users:login') 

@csrf_exempt
def get_attendance_mapped_employees(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    caluserslist = []
    if tok:
        adminrole = (request.session.get('rolename')).lower()
        headers = {'Authorization': t}
        today = datetime.date.today()
        
        if adminrole == "admin" or adminrole == "core team":
            data={}
            data['year'] = today.year
            data['month'] = today.month
            data['UserId'] = request.session['userID']
            userid = request.session['userID']
            firstname = request.session['Firstname']
            lastname = request.session['Lastname']
            userlist = requests.get(userListUrl,headers=headers)
            userresponse = userlist.json()
            
            alldict = {}
            alldict['userid'] = "All"
            alldict['useridstr'] = "All"
            caluserslist.append(alldict)
            
            for i in userresponse['data']:

                userdict = {}
                userdict['userid'] = i['id']
                userdict['useridstr'] = i['Firstname'] +" "+ i['Lastname']
                userdict['Photo'] = i['Photo']
                
                caluserslist.append(userdict)

            context={       
                        "caluserslist":caluserslist,
                    }
            return HttpResponse(json.dumps(context),content_type='application/json')


        else:
            data={}
            data['year'] = today.year
            data['month'] = today.month
            data['UserId'] = request.session['userID']
            userid = request.session['userID']
            firstname = request.session['Firstname']
            lastname = request.session['Lastname']

            taskmappingURL = remoteURL+'users/api/getMappingForUpdate?ManagerID={}'.format(userid)
            taskmappingresponse = requests.get(taskmappingURL, headers = headers)
            taskmappingdata = taskmappingresponse.json()
            caluserslist = []
            
            if taskmappingdata['data'] != '':
                
                alldict = {}
                alldict['userid'] = "All"
                alldict['useridstr'] = "All"
                caluserslist.append(alldict)
                
                for i in taskmappingdata['data']:
                    caldict = {}
                    caldict['userid'] = i['UserID']
                    caldict['useridstr'] = i['UserIDStr']
                    caldict['Photo'] = i['Photo']
                    
                    caluserslist.append(caldict)
            
                userdict = {}
                userdict['userid'] = userid
                userdict['useridstr'] = firstname +" "+lastname
                caluserslist.append(userdict)

                
            else:
                userdict = {}
                userdict['userid'] = userid
                userdict['useridstr'] = firstname +" "+lastname
                caluserslist.append(userdict)
                
            context={
                        "caluserslist":caluserslist,
                    }

            return HttpResponse(json.dumps(context),content_type='application/json')

    else:
        return redirect('users:login') 

@csrf_exempt
def getattendancebydate(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        data={}
        data['my_date']=request.POST.get("my_date")
        userid = request.session['userID']
        adminrole = (request.session.get('rolename')).lower()
        if adminrole == "admin" or adminrole == "core team":
            getattendancebydate_Url = remoteURL+"leave/api/getattendancebydate"
            response1 = requests.post(getattendancebydate_Url,data=data,headers=headers)
            yearly_obj_response = response1.json()
            return HttpResponse(json.dumps({"context":yearly_obj_response['context']}),content_type='application/json')
        else:
            getattendancebydate_Url = remoteURL+"leave/api/getattendancebydate?userid={}".format(userid)
            response1 = requests.post(getattendancebydate_Url,data=data,headers=headers)
            yearly_obj_response = response1.json()
            return HttpResponse(json.dumps({"context":yearly_obj_response['context']}),content_type='application/json')
    else:
        return redirect('users:login') 

@csrf_exempt
def get_leaves_and_latemarks_by_date(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        data={}
        data['start_date']=request.POST.get("start_date")
        data['end_date']=request.POST.get("end_date")
        data['empId']=request.POST.get("empId")

        get_leaves_and_latemarks_by_date_Url = remoteURL+"leave/api/get_leaves_and_latemarks_by_date"
        response1 = requests.post(get_leaves_and_latemarks_by_date_Url,data=data,headers=headers)
        yearly_obj_response = response1.json()
        return HttpResponse(json.dumps({"context":yearly_obj_response['data']}),content_type='application/json')
    else:
        return redirect('users:login') 

@csrf_exempt
def attendance_cal_year_change(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}

        today = datetime.date.today()
        data={}
        data['year'] = today.year
        data['month'] = today.month
        data['UserId'] = request.session['userID']
        userid = request.session['userID']
        adminrole = (request.session.get('rolename')).lower()

        if adminrole == "admin" or adminrole == "core team":
            if request.method == 'POST':
                data['month'] = request.POST.get('month')
                data['year'] = request.POST.get('year')
                data['UserId'] = request.POST.get('empid')

                if data['UserId'] == "All":
                    calendar_allUrl = remoteURL+"leave/api/getattendancecount"
                    response1 = requests.post(calendar_allUrl,data=data,headers=headers)
                    
                    yearly_obj_response = response1.json()
                    return HttpResponse(json.dumps({
                                    "Name":yearly_obj_response['Name'],
                                    "EmployeeId":yearly_obj_response['EmployeeId'],
                                    "Designation":yearly_obj_response['Designation'], 
                                    "Photo":yearly_obj_response['Photo'], 
                                    "UserId" : userid,
                                    "context":yearly_obj_response['context'],
                                }),content_type='application/json')
                    
                    
                    
                    
                else:
                    
                    yearly_obj = requests.post(getyearlydata_url,data=data,headers=headers)
                    yearly_obj_response = yearly_obj.json()
                    return HttpResponse(json.dumps({
                                    "Photo":yearly_obj_response['Photo'], 
                                    "Name":yearly_obj_response['Name'],
                                    "Designation":yearly_obj_response['Designation'], 
                                    "EmployeeId":yearly_obj_response['EmployeeId'],
                                    "monthstr":yearly_obj_response['monthstr'],
                                    "total_6monthly_leave_count":yearly_obj_response['total_6monthly_leave_count'],
                                    "avghour":yearly_obj_response['avghour'],
                                    "monthly_late_count":yearly_obj_response['monthly_late_count_data'],
                                    "UserId" : userid,

                                }),content_type='application/json')
                
        else:
            if request.method == 'POST':
                data['month'] = request.POST.get('month')
                data['year'] = request.POST.get('year')
                data['UserId'] = request.POST.get('empid')
                
                if data['UserId'] == "All":
                    
                    calendar_allUrl = remoteURL+"leave/api/getattendancecount?userid={}".format(userid)
                    response1 = requests.post(calendar_allUrl,data=data,headers=headers)
                    yearly_obj_response = response1.json()
                    return HttpResponse(json.dumps({
                                    "Name":yearly_obj_response['Name'],
                                    "EmployeeId":yearly_obj_response['EmployeeId'],
                                    "Designation":yearly_obj_response['Designation'], 
                                    "Photo":yearly_obj_response['Photo'], 
                                    "UserId" : userid,
                                    "context":yearly_obj_response['context'],
                                }),content_type='application/json')
                    
                else:
                    yearly_obj = requests.post(getyearlydata_url,data=data,headers=headers)
                    yearly_obj_response = yearly_obj.json()

                    return HttpResponse(json.dumps({
                                    "Photo":yearly_obj_response['Photo'], 
                                    "Name":yearly_obj_response['Name'],
                                    "Designation":yearly_obj_response['Designation'], 
                                    "EmployeeId":yearly_obj_response['EmployeeId'],
                                    "monthstr":yearly_obj_response['monthstr'],
                                    "total_6monthly_leave_count":yearly_obj_response['total_6monthly_leave_count'],
                                    "avghour":yearly_obj_response['avghour'],
                                    "monthly_late_count":yearly_obj_response['monthly_late_count_data'],
                                    "UserId" : userid,
                                    
                                    
                                    

                                }),content_type='application/json')
               

    else:
        return redirect('users:login') 

def secondary_info(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    # getCurrUserdata = userforpage(request)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        UserId = request.session.get('userID')
        id=UserId

        Fullname = request.session.get('Firstname')+" "+request.session.get('Lastname')
       
        if request.method == "GET":
            getUserUrl = remoteURL + 'users/api/Employee_allinfo'
            usersRes = requests.get(getUserUrl,headers=headers)
            usersResponse = usersRes.json()
            
            secondaryInfoData = usersResponse['data']['userSecondaryObject']
            educatiopnalqualificationsData = usersResponse['data']['educationdetails']
            previouscompanyData = usersResponse['data']['company_details']

            ssc_qualification = next((q for q in usersResponse['data']['educationdetails'] if q['qualification_name'] == 'SSC'), None)

            HSC_qualification = next((q for q in usersResponse['data']['educationdetails'] if q['qualification_name'] == 'HSC'), None)

            gaduation = next((q for q in usersResponse['data']['educationdetails'] if q['qualification_name'] == 'Graduation/Degree'), None)

            POSTGraduation = next((q for q in usersResponse['data']['educationdetails'] if q['qualification_name'] == 'POST Graduation'), None)

            users = usersResponse['data']['userdata']
            documents = usersResponse['data']['documentlist']

            return render(request, 'admin/employeemaster/updatesecondaryemployee.html',
                          {'Fullname': Fullname,
                           'userID': id,
                           'users': users,
                           'secondaryInfo':secondaryInfoData,
                           'hostUrl':imageURL,
                           'qualifications':educatiopnalqualificationsData,
                           'previouscompanys':previouscompanyData,
                           "ssc_qualification":ssc_qualification,
                           "HSC_qualification":HSC_qualification,
                           "POSTGraduation":POSTGraduation,
                           "gaduation":gaduation,
                           'hostUrl':imageURL ,
                           "documents":documents })
            
            
            
        
        elif request.method == "POST":
            data = {}
            data['userId'] = UserId
            email = request.POST.get('email')
            data['permanentaddress'] = request.POST.get('permanentaddress')
            data['bloodgroup'] = request.POST.get('bloodgroup')
            data['relation1'] = request.POST.get('relation1')
            data['relation1number'] = request.POST.get('relation1number')
            data['relation2'] = request.POST.get('relation2')
            data['relation2number'] = request.POST.get('relation2number')
            data['refname1'] = request.POST.get('refname1')
            data['refdesg1'] = request.POST.get('refdesg1')
            data['refemail1'] = request.POST.get('refemail1')
            data['refname2'] = request.POST.get('refname2')
            data['refdesg2'] = request.POST.get('refdesg2')
            data['refnumber1'] = request.POST.get('refnumber1')
            data['refnumber2'] = request.POST.get('refnumber2')
            data['refemail2'] = request.POST.get('refemail2')
            data['comapanyname'] = request.POST.get('comapanyname')
            data['companyaddress'] = request.POST.get('companyaddress')
            data['bankname'] = request.POST.get('bankname')
            data['ifsccode'] = request.POST.get('ifsccode')
            data['accountnumber'] = request.POST.get('accountnumber')
            data['confirmaccountnumber'] = request.POST.get('confirmaccountnumber')
            data['adhaarcard'] = request.POST.get('adhaarcard')
            adhaarcardimage = request.FILES.get('adhaarcardimage', None)
            pancardimage = request.FILES.get('pancardimage', None)
            photo = request.FILES.get('photo', None)
            data['pancard'] = request.POST.get('pancard')
            updateEmprequest = employeeupdateURL + "?userID=" + str(UserId)
            updateEmpResponse = requests.post(updateEmprequest,headers=headers,data={'email':email},files={'Photo': photo})
            updateEmpData = updateEmpResponse.json()
            postSecondaryInfoUrl = remoteURL + 'users/api/addSecondaryInfo'
            addSecondaryResponse = requests.post(postSecondaryInfoUrl,files={'adhaarcardimage': adhaarcardimage,'pancardimage':pancardimage}, data=data,headers=headers)
            postResponse = addSecondaryResponse.json()
            if postResponse['response']['n'] == 1:
                messages.success(request, postResponse['response']['msg'])
                return redirect('users:dashboard')
            else:
                messages.error(request, postResponse['response']['msg'])
                return redirect('users:dashboard')
    else:
        return redirect('users:login')
    
def secondary_info_ajax(request):
    tok = request.session.get('token', False)
    # getCurrUserdata = userforpage(request)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        UserId = request.GET.get('id')
        if request.method == "GET":
            getUserUrl = remoteURL + 'users/api/getuser?userID={}'.format(UserId)
            usersResponse = requests.get(getUserUrl, headers=headers)
            getSecondaryInfoUrl = remoteURL + 'users/api/getSecondaryInfo?userId={}'.format(UserId)
            getSecondaryInfoResponse =requests.get(getSecondaryInfoUrl)
            secondaryInfoData = getSecondaryInfoResponse.json()
            users = usersResponse.json()
            context={'userID': UserId,'users': users,'secondaryInfo':secondaryInfoData['data'],'hostUrl':imageURL}
            return HttpResponse(json.dumps(context),content_type='application/json')

def forgetpassword(request):

    if request.method == "POST":
        data={}
        data['email'] = request.POST.get('Username')
        forget_password_request = requests.post(forget_password_url,data=data)
        forget_password_response = forget_password_request.json()
        if forget_password_response['n'] == 1:
            messages.success(request,forget_password_response['Msg'])
            return redirect('users:login')
        else:
            messages.warning(request,forget_password_response['Msg'])
            return render(request,'forgetpassword.html')
    return render(request,'forgetpassword.html')

def reset_password(request,id):
    if request.method == "POST":
        data={}
        data['newpassword'] = request.POST.get('newpassword')
        data['token'] = id
        reset_password_request = requests.post(reset_password_url,data=data)
        reset_password_response = reset_password_request.json()
        if reset_password_response['n'] == 1:
            messages.success(request,reset_password_response['Msg'])
            return redirect('users:login')
        else:
            messages.warning(request,reset_password_response['Msg'])
            return render(request,'admin/resetpassword.html')
    return render(request,'admin/resetpassword.html')

def punch_indata(request):
    tok = request.session['token']
    if tok:
        attendanceId =  request.session.get('employeeId')
        
        current_date = datetime.datetime.now().date()  
       
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data = {
            'employeeId':attendanceId,
            'date':current_date,
            'latitude':request.POST.get('latitude'),
            'longitude':request.POST.get('longitude'),
            'Remote_Reason':request.POST.get('Remote_Reason'),

        }
        emp_data = requests.post(punch_inurl,data=data,headers=headers) 
        empid_data = emp_data.json()
        return HttpResponse(json.dumps(empid_data),content_type='application/json')
    else:
        return redirect('users:login')

def punch_outdata(request):
    tok = request.session['token']
    if tok:
        attendanceId =  request.session.get('employeeId')
        current_date = datetime.datetime.now().date()  
       
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data = {
            'employeeId':attendanceId,
            'date':current_date,
            'latitude':request.POST.get('latitude'),
            'longitude':request.POST.get('longitude'),
        }
        emp_data = requests.post(punch_outurl,data=data,headers=headers) 
        empid_data = emp_data.json()
        return HttpResponse(json.dumps(empid_data),content_type='application/json')
    else:
        return redirect('users:login')
  
  
def get_the_user_device_location(request):
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data = {
            'latitude':request.POST.get('latitude'),
            'longitude':request.POST.get('longitude'),
        
        }
        get_the_user_device_location_url= remoteURL + "users/api/get_the_user_device_location"
        emp_data = requests.post(get_the_user_device_location_url,data=data,headers=headers) 
        empid_data = emp_data.json()
        return HttpResponse(json.dumps(empid_data),content_type='application/json')
    else:
        return redirect('users:login')
      
      
      
# def get_the_user_device_location(request):
    
#     tok = request.session['token']
#     if tok:
#         t = 'Token {}'.format(tok)
#         headers = {'Authorization': t}
#         ip_address = 'waruat.onerooftechnologiesllp.com'
#         # ip_address = request.META.get('REMOTE_ADDR')

        
#         # Get location based on IP address
#         if ip_address:
#             geolocator = Nominatim(user_agent="geoapiExercises")
#             location = geolocator.geocode(ip_address)
#             if location:
                
#                 latitude = location.latitude
#                 longitude =location.longitude

        
#                 data = {
#                     # 'latitude':request.POST.get('latitude'),
#                     # 'longitude':request.POST.get('longitude'),
#                     'latitude':latitude,
#                     'longitude':longitude,
                    
#                 }
#                 get_the_user_device_location_url= remoteURL + "users/api/get_the_user_device_location"
#                 location_test_request = requests.post(get_the_user_device_location_url,data=data,headers=headers) 
#                 location_test_response = location_test_request.json()

#                 return HttpResponse(json.dumps(location_test_response),content_type='application/json')
            
#             else:
#                 return HttpResponse(json.dumps({"data":{'location_name':'','location_url':''},"response":{"n" : 0,"msg" : "Failed to fetch location.","status" : "error"}}),content_type='application/json')

#         else:
#             return HttpResponse(json.dumps({"data":{'location_name':'','location_url':''},"response":{"n" : 0,"msg" : "IP address not found.","status" : "error"}}),content_type='application/json')
#     else:
#         return redirect('users:login')
  
      
      
      
      
def get_data(request):
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        employeeId = request.session.get('employeeId')
        current_date = datetime.datetime.now().date()  
        data = {
            'employeeId':employeeId,
            'date':current_date,
        }
        employee_data = requests.get(punch_geturl,data=data,headers=headers) 
        empid_data = employee_data.json()
        return HttpResponse(json.dumps(empid_data),content_type='application/json')
    else:
        return redirect('users:login')



def permission(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('updatepassword/{}/'.format(request.session.get('userID')))

        if request.method == 'POST':
            roleID = request.POST['roleID']
            checkedMenuList = request.POST.getlist('check')

            # delete all permissions regarding this role
            deletePermissionUrl = remoteURL + \
                'users/api/deletepermission?RoleID={}'.format(roleID)
            deletePermission = requests.get(
                deletePermissionUrl, headers=headers)
            Response_ = deletePermission.json()
            # add new permissions
            addPermissionUrl = remoteURL+'users/api/addpermission'
            data = {}
            data['RoleID'] = roleID
            data['MenuID'] = request.POST.getlist('check')
            addPermission = requests.post(
                addPermissionUrl, data=data, headers=headers)
            Response_ = addPermission.json()
            if Response_['response']['n'] == 1:
                messages.success(request,Response_['response']['msg'])
                return redirect('users:permission')
            else:
                messages.warning(request,Response_['response']['msg'])
                return redirect('users:permission')
            
        permissionlist = requests.get(permission_list_url,headers=headers)
        permission_list_response = permissionlist.json()

        menu_list_request = requests.get(menu_list_url,headers=headers)
        menu_list_response = menu_list_request.json()

        role_list_request = requests.get(role_list_url,headers=headers)
        role_list_response = role_list_request.json()

        return render(request,'admin/permission.html',{'menuList':menu_list_response,'roleList':role_list_response['data'],'permissionlist':permission_list_response})
    else:
        return redirect('users:login')

def GetRolePermissions(request):
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        permissionlist = requests.get(permission_list_url,headers=headers)
        permission_list_response = permissionlist.json()

        menu_list_request = requests.get(menu_list_url,headers=headers)
        menu_list_response = menu_list_request.json()

        role_list_request = requests.get(role_list_url,headers=headers)
        role_list_response = role_list_request.json()

        context={
           'menuList':menu_list_response,
            'roleList':role_list_response['data'],
            'permissionlist':permission_list_response
        }
        return HttpResponse(json.dumps(context),content_type='application/json')
    else:
        return redirect('users:login')

def addduplicaterole(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            # add new permissions
            addduplicateroleUrl = remoteURL+'users/api/addduplicateroleapi'
            data = {}
            data['RoleID'] =  request.POST['RoleID']
            addPermission = requests.post(
                addduplicateroleUrl, data=data, headers=headers)
            Response_ = addPermission.json()
            return HttpResponse(json.dumps(Response_),content_type='application/json')
    else:
        return redirect('users:login')

def deleterole(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            deleteroleUrl = remoteURL+'users/api/deleteroleapi'
            data = {}
            data['RoleID'] =  request.POST['RoleID']
            delPermission = requests.post(
                deleteroleUrl, data=data, headers=headers)
            Response_ = delPermission.json()
            return HttpResponse(json.dumps(Response_),content_type='application/json')
    else:
        return redirect('users:login')

def Editrolename(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            editroleUrl = remoteURL+'users/api/editrolenameapi'
            data = {}
            data['RoleID'] =  request.POST['RoleID']
            data['RoleName'] = request.POST['Rolename']
            editPermission = requests.post(
                editroleUrl, data=data, headers=headers)
            Response_ = editPermission.json()
            return HttpResponse(json.dumps(Response_),content_type='application/json')
    else:
        return redirect('users:login')

def updatemultiplerole(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            updatemroleUrl = remoteURL+'users/api/updatemultipleroleapi'
            data = {}
            data['permissionlist'] =  request.POST.get('permissionlist')
            editPermission = requests.post(
                updatemroleUrl, data=data, headers=headers)
            Response_ = editPermission.json()
            return HttpResponse(json.dumps(Response_),content_type='application/json')
    else:
        return redirect('users:login')

def attendance(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 

    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            # file = request.FILES['datafile']
            filedata = requests.post(fileDataUrl,files=request.FILES,headers=headers)
            fileinfo = filedata.json()
            if fileinfo['response']['n']==1:
                messages.success(request,fileinfo['response']['msg'])
            if fileinfo['response']['n']==0:
                messages.warning(request,fileinfo['response']['msg'])
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        return render(request,'admin/Attendance/attendancedata.html')
    else:
        return redirect('users:login')
    
def appendfiledata(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            file = request.FILES['file']
            filedata = requests.post(appendfileDataUrl,files=request.FILES,headers=headers)
            fileinfo = filedata.json()

            # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            return HttpResponse(json.dumps(fileinfo),content_type='application/json')
    else:
        return redirect('users:login')
   
def monthlydata(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['sdate'] = request.POST.get('sdate')
        data['edate'] = request.POST.get('edate')
        empdata = requests.post(monthlydataurl,data=data) 
        empiddata = empdata.json()
        
        return HttpResponse(json.dumps(empiddata),content_type='application/json')
    else:
        return redirect('users:login')

def delete_designation(request,id):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    if tok:
        data={}
        data['id']=id
        delete_request = requests.post(deleteDesgURL, headers=headers,data=data)
        delete_response = delete_request.json()
        messages.success(request,delete_response['response']['msg'])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('users:login')

def delete_location(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['id']=id
        delete_request = requests.post(deleteLocationURL, headers=headers,data=data)
        delete_response = delete_request.json()
        messages.success(request,delete_response['response']['msg'])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('users:login')

def delete_department(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['departmentID']=id
        delete_request = requests.post(deleteDepartURL, headers=headers,data=data)
        delete_response = delete_request.json()
        messages.success(request,delete_response['Msg'])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('users:login')

def getadminholidaydata(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['Month'] = request.POST.get('Month')
            admindsmonthlyholidayurl =  remoteURL + 'users/api/adminmnholidayapi'
            empdata = requests.post(admindsmonthlyholidayurl,data=data,headers=headers) 
            empiddata = empdata.json()
            return HttpResponse(json.dumps(empiddata),content_type='application/json')
    else:
        return redirect('users:login')

def getadminscoredata(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['Week'] = request.POST.get('Week')
            adminmonthlyscoreurl =  remoteURL + 'users/api/adminmonthlyscoreapi'
            empdata = requests.post(adminmonthlyscoreurl,data=data,headers=headers) 
            empiddata = empdata.json()
            if empiddata['data'] !=[]:
                return HttpResponse(json.dumps(empiddata),content_type='application/json')
            else:
                return HttpResponse(json.dumps({}),content_type='application/json')

    else:
        return redirect('users:login')
  
def employee_filter(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}
            data['name'] = request.POST.get('name')      
            data['designation'] = request.POST.get('designation')      
            data['department'] = request.POST.get('department')      
            data['location'] = request.POST.get('location') 
            data['attendance'] = request.POST.get('attendance') 
            response1 = requests.post(employee_filterurl,data=data,headers=headers)          
            leavedata = response1.json()
            return HttpResponse(json.dumps(leavedata),content_type='application/json')
    else:
        return redirect('users:login')
   
def getcompanypackages(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}
            data['companyperiodfilter'] = request.POST.get('companyperiodfilter')      
            companyfilterurl = remoteURL+"company/api/companypackages"
            response1 = requests.post(companyfilterurl,data=data,headers=headers)          
            companydata = response1.json()
            return HttpResponse(json.dumps(companydata),content_type='application/json')
    else:
        return redirect('users:login')

def getSAincomepoints(request):
    tok = request.session.get('token', False)
    if tok :
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        companyincomefilterurl = remoteURL+"company/api/companyyearlyincome"
        response2 = requests.get(companyincomefilterurl,headers=headers)          
        companyincomedata = response2.json()
        return HttpResponse(json.dumps(companyincomedata),content_type='application/json')
    else:
        return redirect('users:login')

def getcompanyleadspoints(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['year']= request.POST.get('year')      
            companyleadsfilterurl = remoteURL+"company/api/companyleadsgraph"
            response2 = requests.post(companyleadsfilterurl,data=data,headers=headers)          
            companyleadsdata = response2.json()
            return HttpResponse(json.dumps(companyleadsdata),content_type='application/json')
    else:
        return redirect('users:login')

def addapproveactionnotf(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['notificationId']= request.POST.get('notificationid')    
            data['Leaveid']= request.POST.get('leaveid')  

            notfurl = remoteURL+"users/api/notfapproveactionapi"
            response2 = requests.post(notfurl,data=data,headers=headers)          
            notfdata = response2.json()
            return HttpResponse(json.dumps(notfdata),content_type='application/json')
    else:
        return redirect('users:login')

def addrejectactionnotf(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['notificationId']= request.POST.get('notificationid')    
            data['Leaveid']= request.POST.get('leaveid')  

            notfurl = remoteURL+"users/api/notfrejectactionapi"
            response2 = requests.post(notfurl,data=data,headers=headers)          
            notfdata = response2.json()
            return HttpResponse(json.dumps(notfdata),content_type='application/json')
    else:
        return redirect('users:login')
    
def filternotificationslist(request):


    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 
    

    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['filtertype']= request.POST.get('notificationtype')   
            notflisturl = remoteURL+"users/api/notffilterlistapi"
            response2 = requests.post(notflisturl,data=data,headers=headers)          
            notfdata = response2.json()
            return HttpResponse(json.dumps(notfdata),content_type='application/json') 
        else:
            # notflisturl = remoteURL+"users/api/notffiltergetlistapi"
            # response3 = requests.get(notflisturl,headers=headers)          
            # notfalldata = response3.json()

            notftypeurl = remoteURL+"users/api/notftypelist"
            response3 = requests.get(notftypeurl,headers=headers)          
            notftypedata = response3.json()

            return render(request,'admin/task/notificationlist.html',{"notftypelist":notftypedata['data']})
    else:
        return redirect('users:login')

def Teamfiltertracker(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['teamfilter']= request.POST.get('teamfilter')   
            teamlisturl = remoteURL+"users/api/teamtrackerdataapi"
            response2 = requests.post(teamlisturl,data=data,headers=headers)          
            notfdata = response2.json()
            return HttpResponse(json.dumps(notfdata),content_type='application/json') 
    else:
       return redirect('users:login')
    
def admin_att_overview(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['weekfilter']= request.POST.get('weekfilter')   
            attoverviewurl = remoteURL+"users/api/admin_attoverview_api"
            response2 = requests.post(attoverviewurl,data=data,headers=headers)          
            notfdata = response2.json()
            return HttpResponse(json.dumps(notfdata),content_type='application/json') 
        else:
            return render(request, 'login.html')
    else:
        return redirect('users:login')
    
def admin_att_list(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data={}
    if request.method == 'POST':
        data['listdatafilter']= request.POST.get('listdatafilter')   
        att_listurl = remoteURL+"users/api/admin_getattlist"
        response2 = requests.post(att_listurl,data=data,headers=headers)          
        notfdata = response2.json()
        return HttpResponse(json.dumps(notfdata),content_type='application/json') 
    else:
        return redirect('users:login')
    
def excel_admin_att_list(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data={}
    if request.method == 'POST':
        data['listdatafilter']= request.POST.get('listdatafilter')   
        att_listurl = remoteURL+"users/api/admin_getattlist"
        response2 = requests.post(att_listurl,data=data,headers=headers)          
        notfdata = response2.json()
        return HttpResponse(json.dumps(notfdata),content_type='application/json') 
    else:
        return redirect('users:login')
    
def admin_attmodal_data(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['weekdatafilter']= request.POST.get('weekmodaldatafilter')  
            data['useridfilter']= request.POST.get('modaluserid')  
            att_listurl = remoteURL+"users/api/admin_attmodaldata"
            response2 = requests.post(att_listurl,data=data,headers=headers)          
            notfdata = response2.json()
            return HttpResponse(json.dumps(notfdata),content_type='application/json') 
    else:
        return render(request, 'login.html')
      
#====================================================================================

def document_verification(request,id):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        id=int(decrypt_parameter(id))
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        Fullname = request.session.get('Firstname')+" "+request.session.get('Lastname')
        data={}
        data['userid']=id

        getUserUrl = remoteURL + 'users/api/Employee_all_info_by_id'
        usersRes = requests.post(getUserUrl,headers=headers,data=data)
        usersResponse = usersRes.json()

        secondaryInfoData = usersResponse['data']['userSecondaryObject']
        educatiopnalqualificationsData = usersResponse['data']['educationdetails']
        previouscompanyData = usersResponse['data']['company_details']

        ssc_qualification = next((q for q in usersResponse['data']['educationdetails'] if q['qualification_name'] == 'SSC'), None)

        HSC_qualification = next((q for q in usersResponse['data']['educationdetails'] if q['qualification_name'] == 'HSC'), None)

        gaduation = next((q for q in usersResponse['data']['educationdetails'] if q['qualification_name'] == 'Graduation/Degree'), None)

        POSTGraduation = next((q for q in usersResponse['data']['educationdetails'] if q['qualification_name'] == 'POST Graduation'), None)

        users = usersResponse['data']['userdata']
        documents = usersResponse['data']['documentlist']

        return render(request, 'admin/employeemaster/documentverification.html',{'Fullname': Fullname,
                                                                                 'userID': id,
                                                                                 'users': users,
                                                                                 'secondaryInfo':secondaryInfoData,'hostUrl':imageURL,'qualifications':educatiopnalqualificationsData,'previouscompanys':previouscompanyData,"ssc_qualification":ssc_qualification,"HSC_qualification":HSC_qualification,"POSTGraduation":POSTGraduation,"gaduation":gaduation,"documents":documents })
    
    
    return redirect('users:login')

def user_secondaryinfo(request,id):
    id = decrypt_parameter(id)
    
    getUserUrl = remoteURL + 'users/api/getuserdetails?userID={}'.format(id)
    usersResponse = requests.get(getUserUrl)
    users = usersResponse.json()

    getSecondaryInfoUrl = remoteURL + 'users/api/getSecondaryInfofordocumentverification?userId={}'.format(id)
    getSecondaryInfoResponse =requests.get(getSecondaryInfoUrl)
    secondaryInfoData = getSecondaryInfoResponse.json()


    getpreviouscompanyUrl = remoteURL + 'users/api/getpreviouscompany?userId={}'.format(id)
    getpreviouscompanyResponse =requests.get(getpreviouscompanyUrl)
    previouscompanyData = getpreviouscompanyResponse.json()

    geteducatiopnalqualificationsUrl = remoteURL + 'users/api/geteducatiopnalqualifications?userId={}'.format(id)
    geteducatiopnalqualificationsResponse =requests.get(geteducatiopnalqualificationsUrl)
    educatiopnalqualificationsData = geteducatiopnalqualificationsResponse.json()

    ssc_qualification = next((q for q in educatiopnalqualificationsData['data'] if q['qualification_name'] == 'SSC'), None)

    HSC_qualification = next((q for q in educatiopnalqualificationsData['data'] if q['qualification_name'] == 'HSC'), None)

    gaduation = next((q for q in educatiopnalqualificationsData['data'] if q['qualification_name'] == 'Graduation/Degree'), None)

    POSTGraduation = next((q for q in educatiopnalqualificationsData['data'] if q['qualification_name'] == 'POST Graduation'), None)


    getcountriesUrl = remoteURL + 'users/api/getecountries'
    getcountriesResponse =requests.get(getcountriesUrl)
    getecountriesData = getcountriesResponse.json()


    empdate = users['data']['linkdatetime'].split('T')[0] + " "+ users['data']['linkdatetime'].split('T')[1].split('+')[0]
    date_format_str = '%Y-%m-%d %H:%M:%S.%f'
    todaysdate = datetime.datetime.today()
    start = datetime.datetime.strptime(empdate, date_format_str)
    diff = todaysdate - start
    # Get interval between two timstamps in hours
    diff_in_hours = diff.total_seconds() / 3600
    if float(diff_in_hours) > 48:
        return render(request,'admin/errorPages/session-expired.html')
    return render(request,'admin/employeemaster/usersecondaryinfo.html',{'userID': id,'users': users,'secondaryInfo':secondaryInfoData['data'],'hostUrl':imageURL,'qualifications':educatiopnalqualificationsData['data'],'previouscompanys':previouscompanyData['data'],"ssc_qualification":ssc_qualification,"HSC_qualification":HSC_qualification,"POSTGraduation":POSTGraduation,"gaduation":gaduation,"countrys":getecountriesData['data'],'hosturl':frontendURL})

def Announcementlist(request):
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
            Annlistreponse = requests.get(announcementurl,headers=headers)   
            Anndata = Annlistreponse.json()
            return render(request, 'admin/masters/Announcements.html',{'Annlist':Anndata['data']})
        else:
            data = {}
            data['announcementText'] = request.POST.get('announcementText')
            data['date'] = request.POST.get('ann_date')
            addannouncementreponse = requests.post(addannouncementURL,headers=headers,data=data)   
            add_anndata = addannouncementreponse.json()
            if add_anndata['response']['n'] == 1:
                messages.success(request,add_anndata['response']['msg'])
                return redirect ('users:Announcementlist')
            else:
                messages.error(request,add_anndata['response']['msg'])
                return redirect ('users:Announcementlist') 
    else:
        return redirect('users:login')
    
def updateAnnouncement(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data ={}
        data['announcementText'] = request.POST.get('announcementText')

        data['date'] = request.POST.get('date')
        date_object = datetime.datetime.strptime(data['date'], '%d-%m-%Y')
        formatted_date = date_object.strftime('%Y-%m-%d')

        data['date'] = formatted_date

        data['id'] = request.POST.get('id')
        update_AnnResponse = requests.post(UpdateAnnouncementURL, headers=headers,data=data)
        updateAnnData = update_AnnResponse.json()
        if updateAnnData['response']['n'] == 1 :
            messages.success(request,updateAnnData['response']['msg'])
        else:
            messages.error(request,updateAnnData['response']['msg'])
        return HttpResponse(json.dumps({'data': updateAnnData}), content_type="application/json")
    else:
        return redirect('users:login')

def delete_Announcement(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['id']=id
        delete_request = requests.post(deleteAnnouncementURL, headers=headers,data=data)
        delete_response = delete_request.json()
        messages.success(request,delete_response['response']['msg'])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('users:login')
    
def lateAttendance(request):
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
            return render(request, 'admin/masters/lateAttendanceReport.html')
    else:
        return redirect('users:login')
      
def onboarding_list(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        onboardinglistResquest = requests.get(onboardinglist_urls,headers=headers)
        onboardinglistResponse = onboardinglistResquest.json()



        return render(request,'admin/employeemaster/non-onboardedlist.html',{'onboardinglist':onboardinglistResponse['data'],"imageURL":imageURL})
    return redirect('users:login')

def onboard_login_password(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['id'] = id
        data['email'] = request.POST.get('email')
        # data['Password'] = request.POST.get('Password')
        onboard_login_passwordResquest = requests.post(onboard_login_password_urls,data=data,headers=headers)
        onboard_login_passwordResponse = onboard_login_passwordResquest.json()
        return HttpResponse(json.dumps(onboard_login_passwordResponse), content_type="application/json") 
    return redirect('users:login') 

def thank_u(request):

    return render(request,'admin/employeemaster/thanku-employee.html')

def accept_document(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        requestdata=request.POST.copy()
        acceptDocumentRequest = requests.post(acceptDocument_urls,data=requestdata,headers=headers)
        acceptDocumentResponse = acceptDocumentRequest.json()
        return HttpResponse(json.dumps(acceptDocumentResponse), content_type="application/json") 
    return redirect('users:login') 

def rejectedDocument(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data1 = []
        requestdata=request.POST.copy()
        rejectedDocumentRequest = requests.post(rejectedDocument_urls,data=requestdata,headers=headers)
        rejectedDocumentResponse = rejectedDocumentRequest.json()
        return HttpResponse(json.dumps(rejectedDocumentResponse), content_type="application/json") 
    return redirect('users:login') 

def updatePersonalDetailsSecondaryInfo(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        requestdata=request.POST.copy()
        updatePersonalDetailsSecondaryInfo_Request = requests.post(updatePersonalDetailsSecondaryInfo_urls,data=requestdata,headers=headers,files=request.FILES)
        updatePersonalDetailsSecondaryInfo_Response = updatePersonalDetailsSecondaryInfo_Request.json()
        return HttpResponse(json.dumps(updatePersonalDetailsSecondaryInfo_Response), content_type="application/json") 
    return redirect('users:login')

def updateEmployeDetailsSecondaryInfo(request):
    tok = request.session.get('token', False)
    
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={} 
        data['id'] = request.POST.get('id')
        data['refname1']=request.POST.get('refname1')
        data['refdesg1']=request.POST.get('refdesg1')
        data['refnumber1']=request.POST.get('refnumber1')
        data['refemail1']=request.POST.get('refemail1')
        data['refname2']=request.POST.get('refname2')
        data['refdesg2']=request.POST.get('refdesg2')
        data['refnumber2']=request.POST.get('refnumber2')
        data['refemail2']=request.POST.get('refemail2')
        data['comapanyname']=request.POST.get('comapanyname')
        data['companyaddress']=request.POST.get('companyaddress')
        updateEmployeDetailsSecondaryInfo_Request = requests.post(updateEmployeDetailsSecondaryInfo_urls,data=data,headers=headers)
        updateEmployeDetailsSecondaryInfo_Response = updateEmployeDetailsSecondaryInfo_Request.json()
        return HttpResponse(json.dumps(updateEmployeDetailsSecondaryInfo_Response), content_type="application/json") 
    return redirect('users:login')

def updateDetailsAndDocument(request):
    tok = request.session.get('token', False)
    
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        requestdata=request.POST.copy()
        # data={}
        # data['id'] = request.POST.get('id')
        # data['bankname']=request.POST.get('bankname')
        # data['ifsccode']=request.POST.get('ifsccode')
        # data['accountnumber']=request.POST.get('accountnumber')
        # data['confirmaccountnumber']=request.POST.get('confirmaccountnumber')
        # data['adhaarcard']=request.POST.get('adhaarcard')
        # data['pancard']=request.POST.get('pancard')
        # data['adhaarcardimage']=request.FILES.get('adhaarcardimage')
        # data['pancardimage']=request.FILES.get('pancardimage')
        updateDetailsAndDocument_Request = requests.post(updateDetailsAndDocument_urls,data=requestdata,headers=headers,files=request.FILES)
        updateDetailsAndDocument_Response = updateDetailsAndDocument_Request.json()
        return HttpResponse(json.dumps(updateDetailsAndDocument_Response), content_type="application/json") 
    return redirect('users:login')

def add_updatePersonalDetailsSecondaryInfo(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        
        requestdata=request.POST.copy()
        updatePersonalDetailsSecondaryInfo_Request = requests.post(updatePersonalDetailsSecondaryInfo_urls,data=requestdata,headers=headers,files=request.FILES)
        updatePersonalDetailsSecondaryInfo_Response = updatePersonalDetailsSecondaryInfo_Request.json()
        return HttpResponse(json.dumps(updatePersonalDetailsSecondaryInfo_Response), content_type="application/json") 
    return HttpResponse(json.dumps({"n":0,"msg":"please login"}), content_type="application/json") 

def add_secondaryInfoLinkApi(request):
    requestdata=request.POST.copy()
    secondaryInfoLinkApi_Request = requests.post(secondaryInfoLinkApi_urls,data=requestdata,files=request.FILES)
    secondaryInfoLinkApi_Response = secondaryInfoLinkApi_Request.json()
    return HttpResponse(json.dumps(secondaryInfoLinkApi_Response), content_type="application/json") 

def add_user_previous_company(request):
    requestdata=request.POST.copy()
    add_user_previous_company_url = remoteURL+"users/api/add_user_previous_company"
    previouscompany_Request = requests.post(add_user_previous_company_url,data=requestdata,files=request.FILES)
    previouscompany_Response = previouscompany_Request.json()
    return HttpResponse(json.dumps(previouscompany_Response), content_type="application/json") 

def edit_user_previous_company(request):
    requestdata=request.POST.copy()
    edit_user_previous_company_url = remoteURL+"users/api/edit_user_previous_company"
    previouscompany_Request = requests.post(edit_user_previous_company_url,data=requestdata,files=request.FILES)
    previouscompany_Response = previouscompany_Request.json()
    return HttpResponse(json.dumps(previouscompany_Response), content_type="application/json") 

def getusercompanydetails(request):
    requestdata=request.POST.copy()
    get_user_previous_company_url = remoteURL+"users/api/get_user_previous_company"
    previouscompany_Request = requests.post(get_user_previous_company_url,data=requestdata,files=request.FILES)
    getpreviouscompany_Response = previouscompany_Request.json()
    return HttpResponse(json.dumps(getpreviouscompany_Response), content_type="application/json")

def deleteusercompanydetails(request):
    requestdata=request.POST.copy()
    delete_user_previous_company_url = remoteURL+"users/api/delete_user_previous_company"
    previouscompany_Request = requests.post(delete_user_previous_company_url,data=requestdata,files=request.FILES)
    getpreviouscompany_Response = previouscompany_Request.json()
    return HttpResponse(json.dumps(getpreviouscompany_Response), content_type="application/json")

def add_educational_qualification_details(request):
    if request.method == 'POST':
        qualificationsArray = json.loads(request.POST.get("qualificationsArray"))
        Photocopylist=request.FILES.getlist("Photocopy")
        files_dict = []
        for file_field in Photocopylist:
            files_dict.append(("image",file_field))

        newlist=[]
        if qualificationsArray:
            for i in qualificationsArray:
                newlist.append(("user",i['userid']))
                newlist.append(("university",i['university']))
                newlist.append(("qualificationname",i['QualificationTitle']))
                newlist.append(("obtainmarks",i['ObtainedMarks']))
                newlist.append(("todate",i['todate']))
                newlist.append(("fromdate",i['fromdate']))


        adddeucationadetails_Request = requests.post(addeducationaldetails_urls,data=newlist,files=request.FILES)
        addeducationaldetails_Response = adddeucationadetails_Request.json()
            
        return HttpResponse(json.dumps(addeducationaldetails_Response), content_type="application/json") 

def add_updateEmployeDetailsSecondaryInfo(request):

    if request.method == 'POST':
        previouscompanydetails = json.loads(request.POST.get("previouscompanydetails"))
        salarysliplist=request.FILES.getlist("salaryslip")
        relievinglist=request.FILES.getlist("relieving")
        userid=request.POST.get('id')

        files_dict = []

        for file_field in salarysliplist:
            files_dict.append(("salaryslip",file_field))

        for file_field in relievinglist:
            files_dict.append(("relieving",file_field))

        newlist=[]
        if previouscompanydetails:
            for i in previouscompanydetails:
                newlist.append(("userid",userid))
                newlist.append(("name",i['name']))
                newlist.append(("designation",i['designation']))
                newlist.append(("address",i['address']))
                newlist.append(("joinDate",i['joinDate']))
                newlist.append(("leaveDate",i['leaveDate']))



        data={}
        data['id']=request.POST.get('id')

        data['refname1']=request.POST.get('refname1')
        data['refdesg1']=request.POST.get('refdesg1')
        data['refnumber1']=request.POST.get('refnumber1')
        data['refemail1']=request.POST.get('refemail1')
        data['refname2']=request.POST.get('refname2')
        data['refdesg2']=request.POST.get('refdesg2')
        data['refnumber2']=request.POST.get('refnumber2')
        data['refemail2']=request.POST.get('refemail2')

        updatecompanyDetailsSecondaryInfo_urls = remoteURL+"users/api/updatecompanydetailssecondaryInfo"

        updatecompanyDetailsSecondaryInfo_Request = requests.post(updatecompanyDetailsSecondaryInfo_urls,data=newlist,files=files_dict)
        updatecompanyDetailsSecondaryInfo_Response = updatecompanyDetailsSecondaryInfo_Request.json()
        
        updateEmployeDetailsSecondaryInfo_Request = requests.post(updateEmployeDetailsSecondaryInfo_urls,data=data)
        updateEmployeDetailsSecondaryInfo_Response = updateEmployeDetailsSecondaryInfo_Request.json()

        return HttpResponse(json.dumps({}), content_type="application/json") 
    
def baseproj_emplist(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        managerid = request.session.get('userID')

        projectListURL = remoteURL + 'project/api/projectLists'
        projectlistreponse = requests.get(projectListURL,headers=headers)   
        projectdata = projectlistreponse.json()

        empurl = remoteURL+'users/api/getMappingForUpdate?ManagerID={}'.format(managerid)
        emplistreponse = requests.get(empurl,headers=headers)   
        empdata = emplistreponse.json()

        context ={
            'projectlist':projectdata['data'],
            'emplist':empdata['data']
        }

        return HttpResponse(json.dumps(context), content_type="application/json")
      
def holidaylist(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "GET":
            holidaylistreponse = requests.get(holidaylisturl,headers=headers)   
            holidaydata = holidaylistreponse.json()
            return HttpResponse(json.dumps(holidaydata), content_type="application/json")
    else:
        return redirect('users:login')
    
def Holidays(request):
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
            hlistreponse = requests.get(holidaylisturl,headers=headers)   
            hhdata = hlistreponse.json()
            return render(request, 'admin/masters/Holidays.html',{'holidaylist':hhdata['data']})
        else:
            data = {}
            data['Date'] = request.POST.get('Date')
            data['Festival'] = request.POST.get('Festival')
            
            holidayreponse = requests.post(addholidayURL,headers=headers,data=data)   
            holdata = holidayreponse.json()
            if holdata['response']['n'] == 1:
                messages.success(request,holdata['response']['msg'])
                return redirect ('users:Holidays')
            else:
                messages.error(request,holdata['response']['msg'])
                return redirect ('users:Holidays') 
    else:
        return redirect('users:login')
    
def updateholidays(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data ={}
        data['Date'] = request.POST.get('Date')
        data['Festival'] = request.POST.get('Festival')
        data['id'] = request.POST.get('id')
        update_holResponse = requests.post(UpdateholidayURL, headers=headers,data=data)
        updateholiData = update_holResponse.json()
     
        if updateholiData['response']['n'] == 1 :
            messages.success(request,updateholiData['response']['msg'])
        else:
            messages.error(request,updateholiData['response']['msg'])
        return HttpResponse(json.dumps({'data': updateholiData}), content_type="application/json")
    else:
        return redirect('users:login')

def delete_holidays(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['id'] = request.POST.get('id')
        delete_request = requests.post(deleteholidayURL, headers=headers,data=data)
        delete_response = delete_request.json()
        messages.success(request,delete_response['response']['msg'])
        return HttpResponse(json.dumps(delete_response), content_type="application/json")
    else:
        return redirect('users:login')
    
def getstatesbycountryid(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "POST":
            data={}
            data['countryid']=request.POST.get('countryid')
            getstatesbycountryidurl = remoteURL+"users/api/getstatesbycountryid"
            statesreponse = requests.post(getstatesbycountryidurl,headers=headers,data=data)   
            statesdata = statesreponse.json()
            return HttpResponse(json.dumps(statesdata), content_type="application/json")
    else:
        return redirect('users:login')
    
def getcitiesbystateid(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "POST":
            data={}
            data['stateid']=request.POST.get('stateid')
            getcitiesbystateidurl = remoteURL+"users/api/getcitiesbystateid"
            citiesreponse = requests.post(getcitiesbystateidurl,headers=headers,data=data)   
            citiesdata = citiesreponse.json()
            return HttpResponse(json.dumps(citiesdata), content_type="application/json")
    else:
        return redirect('users:login')

def OTPEmailsent(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "GET":
            getotpurl = remoteURL+"users/api/updateprofile_otpmail"
            citiesreponse = requests.get(getotpurl,headers=headers)   
            otpdata = citiesreponse.json()
            return HttpResponse(json.dumps(otpdata), content_type="application/json")
    else:
        return redirect('users:login')
    
def Updateprofile(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data ={}

        data['otpnumber'] = request.POST.get('otpnumber')
        data['Phone'] = request.POST.get('mobilenumber')
        data['maritalstatus'] = request.POST.get('maritalstatus')

        data['Address'] = request.POST.get('residentialaddressline1')
        data['Addressline2'] = request.POST.get('residentialaddressline2')
        data['residentialaddresscity'] = request.POST.get('residentialcity')
        data['residentialaddresscountry'] = request.POST.get('residentialcountry')
        data['residentialaddressstate'] = request.POST.get('residentialstate')
        data['residentialaddresspincode'] = request.POST.get('residentialpincode')

        data['permanentaddress'] = request.POST.get('permanentaddressline1')
        data['permanentaddressLine2'] = request.POST.get('permanentaddressline2')
        data['permanantaddresscity'] = request.POST.get('permanentcity')
        data['permanantaddresscountry'] = request.POST.get('permanentcountry')
        data['permanantaddressstate'] = request.POST.get('permanentstate')
        data['permanantaddresspincode'] = request.POST.get('permanentpincode')
       
        UpdateprofileURL = remoteURL+"users/api/updatemyprofile"
        update_profileResponse = requests.post(UpdateprofileURL, headers=headers,data=data,files=request.FILES)
        updateprofileData = update_profileResponse.json()
        userprfileresponse = imageURL + str(updateprofileData['response']['data']['user']['data']['Photo'])
        request.session['userPhoto'] = userprfileresponse
       
        return HttpResponse(json.dumps(updateprofileData), content_type="application/json")
    else:
        return redirect('users:login')

def searchcities(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "POST":
            data={}
            data['cityname'] =  request.POST.get('cityname')
            cityurl = remoteURL+"users/api/searchcity"
            citiesreponse = requests.post(cityurl,data=data,headers=headers)   
            citydata = citiesreponse.json()
            return HttpResponse(json.dumps(citydata), content_type="application/json")
    else:
        return redirect('users:login')

def searchstatecountry(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "POST":
            data={}
            data['cityid'] =  request.POST.get('cityid')
            cityurl = remoteURL+"users/api/getcountrystatebycityid"
            citiesreponse = requests.post(cityurl,data=data,headers=headers)   
            citydata = citiesreponse.json()
            return HttpResponse(json.dumps(citydata), content_type="application/json")
    else:
        return redirect('users:login')

def adminupdate_emp(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        id = request.session.get('userID')
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}


        getUserUrl = remoteURL + 'users/api/getuserdetails?userID={}'.format(id)
        usersResponse = requests.get(getUserUrl)
        users = usersResponse.json()

        getSecondaryInfoUrl = remoteURL + 'users/api/getSecondaryInfofordocumentverification?userId={}'.format(id)
        getSecondaryInfoResponse =requests.get(getSecondaryInfoUrl)
        secondaryInfoData = getSecondaryInfoResponse.json()

        getpreviouscompanyUrl = remoteURL + 'users/api/getpreviouscompany?userId={}'.format(id)
        getpreviouscompanyResponse =requests.get(getpreviouscompanyUrl)
        previouscompanyData = getpreviouscompanyResponse.json()

        geteducatiopnalqualificationsUrl = remoteURL + 'users/api/geteducatiopnalqualifications?userId={}'.format(id)
        geteducatiopnalqualificationsResponse =requests.get(geteducatiopnalqualificationsUrl)
        educatiopnalqualificationsData = geteducatiopnalqualificationsResponse.json()


        return render(request, 'admin/employeemaster/adminupdate_emp.html',{'secondaryInfo':secondaryInfoData['data'],'imageurl':remoteURL,'users': users,'qualifications':educatiopnalqualificationsData['data'],'previouscompanys':previouscompanyData['data'],})
    return redirect('users:login')

def send_onboarding_form(request,id):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        id = int(decrypt_parameter(id))
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "GET":
            stremployeedetailUrl = employeedetailURL + "?userID=" + str(id)
            employeebyiddata = requests.get(stremployeedetailUrl,headers=headers) 
            employeeiddata = employeebyiddata.json()

            deptlistResp = requests.get(departmentUrl, headers=headers)
            deptlistData = deptlistResp.json()

            designatiolistResponse = requests.get(designationListUrl, headers=headers)
            desglistData = designatiolistResponse.json()

            locationlistResponse = requests.get(locationListUrl, headers=headers)
            locationData = locationlistResponse.json()

            rolelistResponse = requests.get(roleListUrl,headers=headers)
            roleData = rolelistResponse.json()
            
            typeofworkdata = [{'id':"1",'type':'Work From Home'},{'id':"2",'type':'Work From Office'},{'id':"3",'type':'Outdoor'},{'id':"4",'type':'Hybrid'}]
            employeestatusdata = [{'statusvalue':'probation','statusName':'Probation'},{'statusvalue':'confirm','statusName':'Confirm'},{'statusvalue':'trainee','statusName':'Trainee'},{'statusvalue':'intern','statusName':'Intern'}]
            return render(request, 'admin/employeemaster/send_onboarding_form.html',{'employeedetails':employeeiddata['data'],'designationlist':desglistData['data'],'deptlist':deptlistData['data'],'locationlist':locationData['data'],'rolelist':roleData['data'],'typelist':typeofworkdata,'statuslist':employeestatusdata})
        else:
            data = {}
            doj = request.POST.get('DateofJoining')
            splitDoj = doj.split('-')
            if len(splitDoj[0]) > 3 :
                data['DateofJoining'] = request.POST.get('DateofJoining')
            else:
                dojstr = '-'.join(reversed(splitDoj))
                data['DateofJoining'] = dojstr

            data['Firstname']=  request.POST.get('firstname')
            data['Lastname']=  request.POST.get('lastname')
            data['password'] = request.POST.get('password')
            data['email'] = request.POST.get('email')
            data['personal_email'] = request.POST.get('personal_email')
            data['DesignationId'] = request.POST.get('designation')
            data['RoleID'] = request.POST.get('role')
            data['DepartmentID'] = request.POST.getlist('DepartmentID')
            data['locationId'] = request.POST.get('location')
            data['Phone'] = request.POST.get('MobileNumber')
            data['typeofwork'] = request.POST.get('typeofwork')
            data['employeeId'] = request.POST.get('employeeId')
            data['employeementStatus'] = request.POST.get('employeeStatus')

            employeesendonboardingURL = remoteURL + 'users/api/sendonboardinglink'
            sendonboardingrequest = employeesendonboardingURL + "?userID=" + str(id)
            sendonboardingresponse = requests.post(sendonboardingrequest,headers=headers,data=data)
            finalresponse = sendonboardingresponse.json()
            if finalresponse['n'] == 1:
                messages.success(request,finalresponse['Msg'])
                return redirect ('users:onboarding-list')
            else:
                messages.error(request,finalresponse['Msg'])
                return redirect ('users:onboarding-list')

def Attendancerequest(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        id = request.session.get('userID')
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "POST":
            data={}
            data['attreason'] = request.POST.get('reason')
            data['requestdate'] = request.POST.get('requestdate')
            data['userid'] = id
            attresponse = requests.post(atturl,data=data,headers=headers)   
            attdata = attresponse.json()
            return HttpResponse(json.dumps(attdata), content_type="application/json")
        else:
            getrequestUrl = remoteURL + 'users/api/getatt_request'
            usersResponse = requests.get(getrequestUrl,headers=headers)
            requesttt = usersResponse.json()

            return render(request, 'admin/Attendance/Attendance_Request.html',{'Pendingrequests':requesttt['data']['pendinglist'],'Approverequests':requesttt['data']['approvedlist'],'Rejectedrequests':requesttt['data']['Rejectedlist'],'Cancelledrequests':requesttt['data']['Cancelledlist']})
    else:
        return redirect('users:login')

def attendanceupdate(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        id = request.session.get('userID')
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "POST":
            data={}
            data['checkin'] = request.POST.get('checkin')
            data['checkout'] = request.POST.get('checkout')
            data['userid'] = id
            attresponse = requests.post(atturl,data=data,headers=headers)   
            attdata = attresponse.json()
            return HttpResponse(json.dumps(attdata), content_type="application/json")
        else:
            return render(request, 'admin/Attendance/Adminatt_Update.html',)
    else:
        return redirect('users:login')

def Attendancerequest_action(request):
    tok = request.session.get('token', False)
    if tok:
        userid = request.session.get('userID')
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}
            data['reqid'] = request.POST.get('id')
            data['Action'] = request.POST.get('action')
            data['usercheckintime'] = request.POST.get('usercheckintime')
            data['usercheckouttime'] = request.POST.get('usercheckouttime')

            attresponse = requests.post(att_actionurl,data=data,headers=headers)   
            attdata = attresponse.json()
            return HttpResponse(json.dumps(attdata), content_type="application/json")
    else:
        return redirect('users:login')
    
def update_employee_first_step(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        requestdata=request.POST.copy()
        update_employee_first_step_urls = remoteURL+"users/api/update_employee_first_step"
        update_employee_first_step_Request = requests.post(update_employee_first_step_urls,data=requestdata,files=request.FILES,headers=headers)
        update_employee_first_step_Response = update_employee_first_step_Request.json()
        return HttpResponse(json.dumps(update_employee_first_step_Response), content_type="application/json") 
    return HttpResponse(json.dumps({"n":0,"msg":"please login"}), content_type="application/json") 




def update_employee_second_step(request):
    if request.method == 'POST':
        qualificationsArray = json.loads(request.POST.get("qualificationsArray"))

        Photocopylist=request.FILES.getlist("Photocopy")
        files_dict = []
        for file_field in Photocopylist:
            files_dict.append(("image",file_field))



        newlist=[]
        if qualificationsArray:
            for i in qualificationsArray:
                newlist.append(("user",i['userid']))
                newlist.append(("university",i['university']))
                newlist.append(("qualificationname",i['QualificationTitle']))
                newlist.append(("obtainmarks",i['ObtainedMarks']))
                newlist.append(("todate",i['todate']))
                newlist.append(("fromdate",i['fromdate']))
                newlist.append(("marksheet",i['Photocopy']))
        update_employee_second_step_urls = remoteURL+"users/api/update_employee_second_step"
        update_employee_second_step_Request = requests.post(update_employee_second_step_urls,data=newlist,files=request.FILES)
        update_employee_second_step_Response = update_employee_second_step_Request.json()
            
        return HttpResponse(json.dumps(update_employee_second_step_Response), content_type="application/json") 

def update_employee_third_step(request):

    if request.method == 'POST':
        previouscompanydetails = json.loads(request.POST.get("previouscompanydetails"))
        salarysliplist=request.FILES.getlist("salaryslip")
        relievinglist=request.FILES.getlist("relieving")
        userid=request.POST.get('id')

        files_dict = []

        for file_field in salarysliplist:
            files_dict.append(("salaryslip",file_field))

        for file_field in relievinglist:
            files_dict.append(("relieving",file_field))

        newlist=[]
        if previouscompanydetails:
            for i in previouscompanydetails:
                newlist.append(("userid",userid))
                newlist.append(("name",i['name']))
                newlist.append(("designation",i['designation']))
                newlist.append(("address",i['address']))
                newlist.append(("joinDate",i['joinDate']))
                newlist.append(("leaveDate",i['leaveDate']))



        data={}
        data['id']=request.POST.get('id')

        data['refname1']=request.POST.get('refname1')
        data['refdesg1']=request.POST.get('refdesg1')
        data['refnumber1']=request.POST.get('refnumber1')
        data['refemail1']=request.POST.get('refemail1')
        data['refname2']=request.POST.get('refname2')
        data['refdesg2']=request.POST.get('refdesg2')
        data['refnumber2']=request.POST.get('refnumber2')
        data['refemail2']=request.POST.get('refemail2')

        updateemployeethirdstepA_urls = remoteURL+"users/api/updatecompanydetailssecondaryInfo"
        updateemployee_thirdA_Request = requests.post(updateemployeethirdstepA_urls,data=newlist,files=files_dict)
        updateemployeerthirdA_Response = updateemployee_thirdA_Request.json()

        update_employee_thgird_B_urls = remoteURL+"users/api/update-employe-details-secondary-info"
        update_employee_thgird_B_Request = requests.post(update_employee_thgird_B_urls,data=data)
        update_employee_thgird_B_Response = update_employee_thgird_B_Request.json()

        return HttpResponse(json.dumps({}), content_type="application/json") 

def update_employee_fourth_step(request):
    requestdata=request.POST.copy()
    update_employee_fourth_step_urls = remoteURL+"users/api/update_employee_fourth_step"

    update_employee_fourth_step_Request = requests.post(update_employee_fourth_step_urls,data=requestdata,files=request.FILES)
    update_employee_fourth_step_Response = update_employee_fourth_step_Request.json()
    return HttpResponse(json.dumps(update_employee_fourth_step_Response), content_type="application/json") 

def update_employee_fifth_step(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        requestdata=request.POST.copy()
        update_employee_fifth_step_urls = remoteURL+"users/api/update_employee_fifth_step"
        update_employee_fifth_step_Request = requests.post(update_employee_fifth_step_urls,data=requestdata,files=request.FILES,headers=headers)
        update_employee_fifth_step_Response = update_employee_fifth_step_Request.json()
        return HttpResponse(json.dumps(update_employee_fifth_step_Response), content_type="application/json") 
    return HttpResponse(json.dumps({"n":0,"msg":"please login"}), content_type="application/json") 

def getrolelist(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        rolelist_request = requests.get(roleListUrl,headers=headers)
        rolelist_response = rolelist_request.json()
        return HttpResponse(json.dumps(rolelist_response), content_type="application/json") 
    else:
        return HttpResponse(json.dumps({'status': 0, 'Msg': 'login required.', 'data': {}}), content_type="application/json") 

def getdesignationlist(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        designationlist_request = requests.get(designationListUrl, headers=headers)
        designationlist_response = designationlist_request.json()
        return HttpResponse(json.dumps(designationlist_response), content_type="application/json") 
    else:
        return HttpResponse(json.dumps({'status': 0, 'Msg': 'login required.', 'data': {}}), content_type="application/json") 

def getdepartmentlist(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        departmentlist_request = requests.get(departmentUrl, headers=headers)
        departmentlist_response = departmentlist_request.json()
        return HttpResponse(json.dumps(departmentlist_response), content_type="application/json") 
    else:
        return HttpResponse(json.dumps({'status': 0, 'Msg': 'login required.', 'data': {}}), content_type="application/json") 

def getlocationlist(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        locationlist_request = requests.get(locationListUrl, headers=headers)
        locationlist_response = locationlist_request.json()
        return HttpResponse(json.dumps(locationlist_response), content_type="application/json") 
    else:
        return HttpResponse(json.dumps({'status': 0, 'Msg': 'login required.', 'data': {}}), content_type="application/json") 

def update_multiple_employee(request,id):
    
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    

    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        id=int(decrypt_parameter(id))
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "GET":

            Employee_all_info_by_idURL = remoteURL + 'users/api/Employee_all_info_by_id'
            data={}
            data['userid']=id
            employeebyiddata = requests.post(Employee_all_info_by_idURL,data=data,headers=headers) 
            employeeiddata = employeebyiddata.json()
            ssc_qualification = next((q for q in employeeiddata['data']['educationdetails'] if q['qualification_name'] == 'SSC'), None)

            HSC_qualification = next((q for q in employeeiddata['data']['educationdetails'] if q['qualification_name'] == 'HSC'), None)

            gaduation = next((q for q in employeeiddata['data']['educationdetails'] if q['qualification_name'] == 'Graduation/Degree'), None)

            POSTGraduation = next((q for q in employeeiddata['data']['educationdetails'] if q['qualification_name'] == 'POST Graduation'), None)







            
            context={
                        'employeedetails':employeeiddata['data'],
                        'hostUrl':imageURL,
                        'userID':id,
                        "ssc_qualification":ssc_qualification,
                        "HSC_qualification":HSC_qualification,
                        "POSTGraduation":POSTGraduation,
                        "gaduation":gaduation,


                        
                    }


            # context={}
            return render(request, 'admin/employeemaster/update_multiple_employees.html',context)
        else:
            data = {}
            doj = request.POST.get('DateofJoining')
            splitDoj = doj.split('-')
            if len(splitDoj[0]) > 3 :
                data['DateofJoining'] = request.POST.get('DateofJoining')
            else:
                dojstr = '-'.join(reversed(splitDoj))
                data['DateofJoining'] = dojstr

            dob = request.POST.get('DateofBirth')
            splitDob = dob.split('-')
            if len(splitDob[0]) > 3 :
                data['BirthDate'] = request.POST.get('DateofBirth')
            else:
                dobstr = '-'.join(reversed(splitDob))
                data['BirthDate'] = dobstr
                
            data['Firstname']=  request.POST.get('firstname')
            data['Lastname']=  request.POST.get('lastname')
            data['password'] = request.POST.get('password')
            data['email'] = request.POST.get('email')
            data['DesignationId'] = request.POST.get('designation')
            data['RoleID'] = request.POST.get('role')
            data['DepartmentID'] = request.POST.getlist('DepartmentID')
            data['locationId'] = request.POST.get('location')
            data['Phone'] = request.POST.get('MobileNumber')
            data['typeofwork'] = request.POST.get('typeofwork')
            data['employeeId'] = request.POST.get('employeeId')
            data['employeementStatus'] = request.POST.get('employeeStatus')
            strupdateUserURL = employeeupdateURL + "?userID=" + str(id)
            addEmpResponse = requests.post(strupdateUserURL,headers=headers,data=data)
            addEmpData = addEmpResponse.json()
            if addEmpData['n'] == 1:
                messages.success(request,addEmpData['Msg'])
                return redirect ('users:employeelist')
            else:
                messages.error(request,addEmpData['Msg'])
                return redirect ('users:employeelist')

def Employeerequest(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 
    tok = request.session.get('token', False)
    if tok:
        userid = request.session.get('userID')
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "POST":
            data={}
            data['request_id'] = request.POST.get('request_id')
            data['Reason'] = request.POST.get('Reason')
            url = remoteURL+'users/api/updateattendancerequestreason'
            Response_ = requests.post(url, data=data, headers=headers)
            response_data = Response_.json()
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            getemprequestUrl = remoteURL + 'users/api/getemp_requestapi'
            usersResponse = requests.get(getemprequestUrl,headers=headers)
            requesttt = usersResponse.json()

            return render(request, 'admin/Attendance/Empattendance_Request.html',{'Pendingrequests':requesttt['data']['pendinglist'],'Approverequests':requesttt['data']['approvedlist'],'Rejectedrequests':requesttt['data']['Rejectedlist'],'Cancelledrequests':requesttt['data']['cancelledlist']})
    else:
        return redirect('users:login')

def get_late_count_per_month(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data=request.data.copy()
        get_late_count_per_month_Url = remoteURL + 'leave/api/get_late_count_per_month'
        get_late_count_per_month_request = requests.get(get_late_count_per_month_Url,data=data, headers=headers)
        get_late_count_per_month_response = get_late_count_per_month_request.json()
        return HttpResponse(json.dumps(get_late_count_per_month_response), content_type="application/json") 
    else:
        return HttpResponse(json.dumps({'status': 0, 'Msg': 'login required.', 'data': {}}), content_type="application/json") 

def cancelattendaancerequest(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data = {}
        if request.method == 'POST':
            data['request_id'] = request.POST.get('request_id')
            url = remoteURL+'users/api/cancelattendancerequest'
            Response_ = requests.post(url, data=data, headers=headers)
            response_data = Response_.json()
            
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return HttpResponse({'n': 0}, content_type="application/json")
    else:
        return redirect('users:login')

def emplist(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            data={}
            data['username']=request.POST.get('username')
            employeelisturl = remoteURL + "users/api/search_by_name_employee"

            request_ = requests.post(employeelisturl,data=data,headers=headers)
            response_data = request_.json()
            
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return HttpResponse({'n': 0,'msg':"Method not allowed"}, content_type="application/json")
    else:
        return HttpResponse({'n': 0,'msg':"login required"}, content_type="application/json")    

def get_emp_by_id(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            data={}
            data['managerid']=request.POST.get('managerid')
            employeedataurl = remoteURL + "users/api/search_emp_by_id"

            request_ = requests.post(employeedataurl,data=data,headers=headers)
            response_data = request_.json()
            
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return HttpResponse({'n': 0,'msg':"Method not allowed"}, content_type="application/json")
    else:
        return HttpResponse({'n': 0,'msg':"login required"}, content_type="application/json")    

def get_user_dashboard(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            employeedataurl = remoteURL + "users/api/getusedashboardata"
            request_ = requests.post(employeedataurl,data=request.POST,headers=headers)
            response_data = request_.json()
            
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return HttpResponse({'n': 0,'msg':"Method not allowed"}, content_type="application/json")
    else:
        return HttpResponse({'n': 0,'msg':"login required"}, content_type="application/json")
    
def checksession(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        checksessionurl = remoteURL + "users/api/checksession"
        checksession_request_ = requests.get(checksessionurl,headers=headers)
        if checksession_request_.status_code == 200:
            return False
        else:
            return True
    else:
       return True

def shiftmaster(request):
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
 
        get_shift_url = remoteURL+"users/api/get_all_shifts"
        shiftrequest = requests.get(get_shift_url,headers=headers)          
        shiftresponse = shiftrequest.json()
        context={
            "shifts":shiftresponse['data']
        }
        return render(request, 'admin/shiftmaster/shift.html',context)


    else:
        return render(request, 'login.html')
    
def add_shift(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['shiftname']= request.POST.get('shiftname')  
            data['outtime']= request.POST.get('outtime')  
            data['intime']= request.POST.get('intime')  
            add_shift_url = remoteURL+"users/api/add_shift"
            add_shift_request = requests.post(add_shift_url,data=data,headers=headers)          
            add_shift_response = add_shift_request.json()
            return HttpResponse(json.dumps(add_shift_response),content_type='application/json') 
    return HttpResponse(json.dumps({"n":0,"msg":"please login again","status":"failed"}),content_type='application/json') 
        
def delete_shift(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['id']= request.POST.get('id')  

            delete_shift_url = remoteURL+"users/api/delete_shift"
            delete_shift_request = requests.post(delete_shift_url,data=data,headers=headers)          
            delete_shift_response = delete_shift_request.json()
            return HttpResponse(json.dumps(delete_shift_response),content_type='application/json') 
    return HttpResponse(json.dumps({"n":0,"msg":"please login again","status":"failed"}),content_type='application/json') 
     
def get_shift_details(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['id']= request.POST.get('id')  
            get_shift_details_url = remoteURL+"users/api/get_shift_details"
            get_shift_details_request = requests.post(get_shift_details_url,data=data,headers=headers)          
            get_shift_details_response = get_shift_details_request.json()
            return HttpResponse(json.dumps(get_shift_details_response),content_type='application/json') 
    return HttpResponse(json.dumps({"n":0,"msg":"please login again","status":"failed"}),content_type='application/json') 

def add_empshiftdetails(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['employee_name']= request.POST.get('employee_name')  
            data['employeeId']= request.POST.get('employeeId')  

            add_empshiftdetails_url = remoteURL+"users/api/add_empshiftdetails"
            add_empshiftdetails_request = requests.post(add_empshiftdetails_url,data=data,headers=headers)          
            add_empshiftdetails_response = add_empshiftdetails_request.json()
            return HttpResponse(json.dumps(add_empshiftdetails_response),content_type='application/json') 
    return HttpResponse(json.dumps({"n":0,"msg":"please login again","status":"failed"}),content_type='application/json') 
        
def delete_empshiftdetails(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['id']= request.POST.get('id')  

            delete_empshiftdetails_url = remoteURL+"users/api/delete_empshiftdetails"
            delete_empshiftdetails_request = requests.post(delete_empshiftdetails_url,data=data,headers=headers)          
            delete_empshiftdetails_response = delete_empshiftdetails_request.json()
            return HttpResponse(json.dumps(delete_empshiftdetails_response),content_type='application/json') 
    return HttpResponse(json.dumps({"n":0,"msg":"please login again","status":"failed"}),content_type='application/json') 
      
def update_shift(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['id']= request.POST.get('id')  
            data['shiftname']= request.POST.get('shiftname')  
            data['outtime']= request.POST.get('outtime')  
            data['intime']= request.POST.get('intime')  
            update_shift_url = remoteURL+"users/api/update_shift"
            update_shift_request = requests.post(update_shift_url,data=data,headers=headers)          
            update_shift_response = update_shift_request.json()
            return HttpResponse(json.dumps(update_shift_response),content_type='application/json') 
    return HttpResponse(json.dumps({"n":0,"msg":"please login again","status":"failed"}),content_type='application/json') 
       
def empshiftmaster(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        
        get_empshiftsdetails_url = remoteURL+"users/api/get_all_empshiftsdetails"
        empshiftsdetailsrequest = requests.get(get_empshiftsdetails_url,headers=headers)          
        empshiftsdetailsresponse = empshiftsdetailsrequest.json()
        
        employeelistResponse = requests.get(userListUrl, headers=headers)
        employeelistData = employeelistResponse.json()
        
        context={
            "empshiftsdetails":empshiftsdetailsresponse['data'],
            "employees":employeelistData['data']
        }

        return render(request, 'admin/shiftmaster/employeeshiftdetails.html',context)


    else:
        return render(request, 'login.html')
        
def shiftallotment(request):
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
        
        
        get_empshiftsdetails_url = remoteURL+"users/api/get_all_empshiftsdetails"
        empshiftsdetailsrequest = requests.get(get_empshiftsdetails_url,headers=headers)          
        empshiftsdetailsresponse = empshiftsdetailsrequest.json()


        get_shift_url = remoteURL+"users/api/get_all_shifts"
        shiftrequest = requests.get(get_shift_url,headers=headers)          
        shiftresponse = shiftrequest.json()

        context={
            "empshiftsdetails":empshiftsdetailsresponse['data'],
            "shifts":shiftresponse['data'],
        }

        return render(request, 'admin/shiftmaster/shiftallotment.html',context)


    else:
        return render(request, 'login.html')
   
@csrf_exempt
def paginationshiftallotmentlist(request):
    if request.session.get('PasswordChanged')==False:
        return redirect('users:updatepassword',id=request.session.get('userID'))
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok) 
        headers = {'Authorization': t}
        if request.method=="POST":
            data={}
            data['employee_name']=request.POST.get('employee_name')
            data['shiftallotmentname']=request.POST.get('shiftallotmentname')
            input_date_object=request.POST.get('searchdate')
            if input_date_object is not None and input_date_object !='':
                output_date  = datetime.datetime.strptime(input_date_object, '%d-%m-%Y')
                data['searchdate'] = output_date.strftime('%Y-%m-%d')
            else:
                data['searchdate'] = ''
            p= request.POST.get('p')
            paginationshiftallotmentListURL = remoteURL + 'users/api/paginationshiftallotmentlist'
            shiftallotmentnewDetailUrlpagination = paginationshiftallotmentListURL + "?p=" +str(p)
            shiftallotmentDetailRequest=requests.post(shiftallotmentnewDetailUrlpagination,data=data,headers=headers)
            shiftallotmentData=shiftallotmentDetailRequest.json()


            return HttpResponse(json.dumps({"shiftallotmentData":shiftallotmentData}),content_type="application/json")
    else:
        return redirect('users:login')

def add_empshiftallotment(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        
        if request.method == 'POST':
            data=request.POST.copy()
            add_empshiftallotment_url = remoteURL+"users/api/add_empshiftallotment"
            add_empshiftallotment_request = requests.post(add_empshiftallotment_url,data=data,headers=headers)          
            add_empshiftallotment_response = add_empshiftallotment_request.json()
            return HttpResponse(json.dumps(add_empshiftallotment_response),content_type='application/json') 
    return HttpResponse(json.dumps({"n":0,"msg":"please login again","status":"failed"}),content_type='application/json') 



def shiftcalenderdashboard(request):
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
 
        # get_shift_url = remoteURL+"users/api/get_all_shifts"
        # shiftrequest = requests.get(get_shift_url,headers=headers)          
        # shiftresponse = shiftrequest.json()
        context={
            # "shifts":shiftresponse['data']
        }
        return render(request, 'admin/shiftmaster/shiftcalenderdashboard.html',context)


    else:
        return render(request, 'login.html')
    


def bulkuploadshiftallotment(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        
        if request.method == 'POST':
            bulkuploadshiftallotment_url = remoteURL+"users/api/bulkuploadshiftallotment"
            bulkuploadshiftallotment_request = requests.post(bulkuploadshiftallotment_url,files=request.FILES,headers=headers)          
            bulkuploadshiftallotment_response = bulkuploadshiftallotment_request.json()
            return HttpResponse(json.dumps(bulkuploadshiftallotment_response),content_type='application/json') 
    return HttpResponse(json.dumps({"n":0,"msg":"please login again","status":"failed"}),content_type='application/json') 
        



        
def delete_empshiftallotment(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        if request.method == 'POST':
            data['id']= request.POST.get('id')  

            delete_empshiftallotment_url = remoteURL+"users/api/delete_empshiftallotment"
            delete_empshiftallotment_request = requests.post(delete_empshiftallotment_url,data=data,headers=headers)          
            delete_empshiftallotment_response = delete_empshiftallotment_request.json()
            return HttpResponse(json.dumps(delete_empshiftallotment_response),content_type='application/json') 
    return HttpResponse(json.dumps({"n":0,"msg":"please login again","status":"failed"}),content_type='application/json') 
     
@csrf_exempt
def employeeshifthistory(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        today = datetime.date.today()
        if checksession(request):
            messages.error(request,'Session expired !')
            return redirect ('users:login') 
        
        Menu = request.session['Menu']
        url = request.path
        access = accessToPage(Menu, url)
        if access == False:
            return redirect('users:accessDenied')
        



        data={}
        data['year'] = today.year
        data['month'] = today.month
        data['UserId'] = request.session['userID']
        userid = request.session['userID']
        firstname = request.session['Firstname']
        lastname = request.session['Lastname']
        username= firstname + ' ' + lastname

        if request.method == 'POST':
            data['month'] = request.POST.get('month')
            data['year'] = request.POST.get('year')
            data['UserId'] = request.POST.get('empid')
            if data['UserId'] == "All":
                calendar_allUrl = remoteURL+"leave/api/getattendancecount"
                response1 = requests.post(calendar_allUrl,data=data,headers=headers)
                caldata = response1.json()
            else:
                response1 = requests.post(calendarUrl,data=data,headers=headers)
                caldata = response1.json()
            return HttpResponse(json.dumps(caldata),content_type='application/json')




        context={       
                    "CoreTeam":True,
                    "UserId" : userid,
                    "username":username,
                }
        
        return render(request,'admin/shiftmaster/employeeshifthistory.html',context
                    )



    else:
        return redirect('users:login') 

@csrf_exempt
def get_all_shifts_employees(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        get_all_shifts_employees_url = remoteURL+"users/api/get_all_shifts_employees"
        get_all_shifts_employees_request = requests.get(get_all_shifts_employees_url,headers=headers)          
        get_all_shifts_employees_response = get_all_shifts_employees_request.json()
        context={       
                    "caluserslist":get_all_shifts_employees_response['data'],
                }
        return HttpResponse(json.dumps(context),content_type='application/json')



    else:
        return redirect('users:login') 

@csrf_exempt
def get_sift_emp_attendance_by_date(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        data={}
        data['my_date']=request.POST.get("my_date")
        getattendancebydate_Url = remoteURL+"leave/api/get_sift_emp_attendance_by_date"
        response1 = requests.post(getattendancebydate_Url,data=data,headers=headers)
        yearly_obj_response = response1.json()
        return HttpResponse(json.dumps({"context":yearly_obj_response['context']}),content_type='application/json')
    else:
        return redirect('users:login') 
    
    
    
@csrf_exempt
def get_all_emp_attendance_by_date(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        data={}
        data['my_date']=request.POST.get("my_date")
        getattendancebydate_Url = remoteURL+"leave/api/get_all_emp_attendance_by_date"
        response1 = requests.post(getattendancebydate_Url,data=data,headers=headers)
        yearly_obj_response = response1.json()
        return HttpResponse(json.dumps({"context":yearly_obj_response['context']}),content_type='application/json')
    else:
        return redirect('users:login') 
@csrf_exempt
def get_sift_emp_attendance_and_task_by_date(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        data={}
        data['shiftid']=request.POST.get("shiftid")
        data['my_date']=request.POST.get("my_date")
        getattendancebydate_Url = remoteURL+"leave/api/get_sift_emp_attendance_and_task_by_date"
        response1 = requests.post(getattendancebydate_Url,data=data,headers=headers)
        yearly_obj_response = response1.json()
        return HttpResponse(json.dumps({"context":yearly_obj_response['context']}),content_type='application/json')
    else:
        return redirect('users:login') 
@csrf_exempt
def get_alloted_shift_header_details(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}

        today = datetime.date.today()
        data={}
        data['year'] = today.year
        data['month'] = today.month

        data['UserId'] = request.session['userID']
        userid = request.session['userID']

    
        if request.method == 'POST':
            data['month'] = request.POST.get('month')
            data['year'] = request.POST.get('year')
            data['UserId'] = request.POST.get('empid')
            
            if data['UserId'] == "All":
                
                calendar_allUrl = remoteURL+"leave/api/get_alloted_shift_header_details"
                response1 = requests.post(calendar_allUrl,data=data,headers=headers)
                yearly_obj_response = response1.json()
                return HttpResponse(json.dumps({
                                "Name":yearly_obj_response['Name'],
                                "EmployeeId":yearly_obj_response['EmployeeId'],
                                "Designation":yearly_obj_response['Designation'], 
                                "Photo":yearly_obj_response['Photo'], 
                                "UserId" : userid,
                                "context":yearly_obj_response['context'],
                            }),content_type='application/json')
                
            else:
                data['userid']=data['UserId']
                get_empinfo_url=remoteURL+"users/api/Employee_all_info_by_id"
                yearly_obj = requests.post(get_empinfo_url,data=data,headers=headers)
                yearly_obj_response = yearly_obj.json()
                if yearly_obj_response['data']['userdata']['Photo'] is not None and yearly_obj_response['data']['userdata']['Photo'] !="" and yearly_obj_response['data']['userdata']['Photo']!="None":
                    profileimage=imageURL+str(yearly_obj_response['data']['userdata']['Photo'])
                else:
                    profileimage=imageURL+'/static/assets/images/profile.png'

                return HttpResponse(json.dumps({
                                
                                "Name":yearly_obj_response['data']['userdata']['Firstname'] + " " + yearly_obj_response['data']['userdata']['Lastname'],
                                "EmployeeId":yearly_obj_response['data']['userdata']['employeeId'],
                                "Designation":yearly_obj_response['data']['userdata']['DesignationId'], 
                                "Photo":profileimage, 
                                "UserId" :yearly_obj_response['data']['userdata']['id'],
                               

                            }),content_type='application/json')
            

    else:
        return redirect('users:login') 

@csrf_exempt
def shift_history_by_month(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        today = datetime.date.today()
        if checksession(request):
            messages.error(request,'Session expired !')
            return redirect ('users:login') 


        data={}
        data['year'] = today.year
        data['month'] = today.month
        data['UserId'] = request.session['userID']
        userid = request.session['userID']
        if request.method == 'POST':
            data['month'] = request.POST.get('month')
            data['year'] = request.POST.get('year')
            data['UserId'] = request.POST.get('empid')
            if data['UserId'] == "All":
                calendar_allUrl = remoteURL+"leave/api/get_daily_attendance_by_month"
                response1 = requests.post(calendar_allUrl,data=data,headers=headers)
                caldata = response1.json()
            else:
                emp_monthly_shift_details_url = remoteURL+"users/api/emp_monthly_shift_details"
                response1 = requests.post(emp_monthly_shift_details_url,data=data,headers=headers)
                caldata = response1.json()
            return HttpResponse(json.dumps(caldata),content_type='application/json')
        
        


    else:
        return redirect('users:login') 




@csrf_exempt
def getcalendershedule(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        if checksession(request):
            messages.error(request,'Session expired !')
            return redirect ('users:login') 
        if request.method == 'POST':
            data={}
            data['year']=request.POST.get('year')
            data['month']=request.POST.get('month')

            dashboardcalenderurl = remoteURL+"users/api/dashboardcalender"
            dashboardcalender_request = requests.post(dashboardcalenderurl,data=data,headers=headers)
            dashboardcalender_response = dashboardcalender_request.json()
            return HttpResponse(json.dumps(dashboardcalender_response),content_type='application/json')
    else:
        return redirect('users:login') 



@csrf_exempt
def change_working_status(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        if checksession(request):
            messages.error(request,'Session expired !')
            return redirect ('users:login') 
        if request.method == 'POST':
            data={}
            data['status']=request.POST.get('status')
            data['task_notification_id']=request.POST.get('task_notification_id')
            change_working_statusurl = remoteURL+"leave/api/change_working_status"
            change_working_status_request = requests.post(change_working_statusurl,data=data,headers=headers)
            change_working_status_response = change_working_status_request.json()
            return HttpResponse(json.dumps(change_working_status_response),content_type='application/json')
    else:
        return redirect('users:login') 
    
def mark_forced_system_checkout(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        if checksession(request):
            messages.error(request,'Session expired !')
            return redirect ('users:login') 
        if request.method == 'POST':
            data={}
            data['status']=request.POST.get('status')
            
            mark_forced_system_checkouturl = remoteURL+"leave/api/mark_forced_system_checkout"
            mark_forced_system_checkout_request = requests.post(mark_forced_system_checkouturl,data=data,headers=headers)
            mark_forced_system_checkout_response = mark_forced_system_checkout_request.json()
            return HttpResponse(json.dumps(mark_forced_system_checkout_response),content_type='application/json')
    else:
        return redirect('users:login') 



def employeetypemaster(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "POST":
            data={}
            data['employeetype'] = request.POST.get('employeetype')
            add_employeetypeurl = remoteURL+'users/api/add_employeetype'
            Response_ = requests.post(add_employeetypeurl, data=data, headers=headers)
            response_data = Response_.json()
            if response_data['n'] ==1:
                messages.success(request, response_data['msg'])
                return redirect('users:employeetypemaster')
                
            else:
                messages.error(request, response_data['msg'])
                return redirect('users:employeetypemaster')
        else:
            getemployeetyperequestUrl = remoteURL + 'users/api/get_all_employeetype'
            employeetypeResponse = requests.get(getemployeetyperequestUrl,headers=headers)
            requesttt = employeetypeResponse.json()
            return render(request, 'admin/masters/employeetypemaster.html',{'employeetypes':requesttt['data']})
    else:
        return redirect('users:login')






def updateemployeetype(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}

        if request.method == "POST":
            data={}
            data['employeetype'] = request.POST.get('employeetype')
            data['id'] = request.POST.get('id')
            update_employeetypeurl = remoteURL+'users/api/update_employeetype'
            Response_ = requests.post(update_employeetypeurl, data=data, headers=headers)
            response_data = Response_.json()
            return HttpResponse(json.dumps(response_data),content_type='application/json')

    else:
        return redirect('users:login')

def delete_employeetype(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}

        if request.method == "POST":
            data={}
            data['id'] = request.POST.get('id')
            delete_employeetypeurl = remoteURL+'users/api/delete_employeetype'
            Response_ = requests.post(delete_employeetypeurl, data=data, headers=headers)
            response_data = Response_.json()
            return HttpResponse(json.dumps(response_data),content_type='application/json')

    else:
        return redirect('users:login')
    
    
def getemployeetypelist(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}

        if request.method == "POST":
            get_all_employeetypeurl = remoteURL+'users/api/get_all_employeetype'
            Response_ = requests.get(get_all_employeetypeurl,headers=headers)
            response_data = Response_.json()
            return HttpResponse(json.dumps(response_data),content_type='application/json')
    else:
        return redirect('users:login')
    
def typerules(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}
            data['TypeId'] = request.POST.get('emptype')
            data['Shifts'] = request.POST.getlist('shifttype')
            data['CompOff'] = request.POST.get('compoff')
            data['CompOffTime'] = request.POST.get('compofftime')
            data['CompOffValidity'] = request.POST.get('compoffvalidity')

            add_typeurl = remoteURL+'users/api/Addtyperules'
            Response_ = requests.post(add_typeurl, data=data, headers=headers)
            response_data = Response_.json()
            if response_data['n']==1:
                messages.success(request, response_data['msg'])
            else:
                messages.error(request, response_data['msg'])
            
            return redirect('users:typerules')
        
        else:
            getemployeetypeUrl = remoteURL + 'users/api/get_all_employeetype'
            employeetypeResponse = requests.get(getemployeetypeUrl,headers=headers)
            requesttt = employeetypeResponse.json()

            shiftURL =  remoteURL + 'users/api/get_all_shifts'
            shiftResponse = requests.get(shiftURL,headers=headers)
            shiftresp = shiftResponse.json()

            rulestypeurl = remoteURL + 'users/api/gettyperules'
            rulestypeResponse = requests.get(rulestypeurl,headers=headers)
            rulestyperesp = rulestypeResponse.json()

            return render(request, 'admin/masters/RuleBuilder.html',{'emptype':requesttt['data'],'shifttypes':shiftresp['data'],'typeruleslist':rulestyperesp['data']})
    else:
        return redirect('users:login')


def update_employee_type_rules(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data=request.POST.copy()
            add_typeurl = remoteURL+'users/api/Updatetyperules'
            Response_ = requests.post(add_typeurl, data=data, headers=headers)
            response_data = Response_.json()
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return HttpResponse({'n': 0,'msg':"Method not allowed"}, content_type="application/json")
    else:
        return HttpResponse({'n': 0,'msg':"login required"}, content_type="application/json")    
        
def delete_employee_type_rules(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data=request.POST.copy()
            delete_typeurl = remoteURL+'users/api/delete_employee_type_rules'
            Response_ = requests.post(delete_typeurl, data=data, headers=headers)
            response_data = Response_.json()

            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return HttpResponse({'n': 0,'msg':"Method not allowed"}, content_type="application/json")
    else:
        return HttpResponse({'n': 0,'msg':"login required"}, content_type="application/json")
    
    
@csrf_exempt
def getshiftevents(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            getshifteventsurl = remoteURL + "users/api/getshiftevents"
            data=request.POST.copy()
            request_ = requests.post(getshifteventsurl,headers=headers,data=data)
            response_data = request_.json()
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return HttpResponse({'n': 0,'msg':"Method not allowed"}, content_type="application/json")
    else:
        return HttpResponse({'n': 0,'msg':"login required"}, content_type="application/json")    



@csrf_exempt
def shiftexcelreport(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}

        shiftexcelreporturl = remoteURL + 'users/api/shiftexcelreport'
        
        empdata = requests.post(shiftexcelreporturl,data=request.POST) 
        empiddata = empdata.json()
        
        return HttpResponse(json.dumps(empiddata),content_type='application/json')
    else:
        return redirect('users:login')
    
@csrf_exempt
def attendanceexcelreport(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}

        attendanceexcelreporturl = remoteURL + 'users/api/attendanceexcelreport'
        
        empdata = requests.post(attendanceexcelreporturl,data=request.POST) 
        empiddata = empdata.json()
        
        return HttpResponse(json.dumps(empiddata),content_type='application/json')
    else:
        return redirect('users:login')
    
def getemployeeallotedshift(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data=request.POST.copy()
            
            if data['shiftdate'] is not None and data['shiftdate'] !='':
                output_date  = datetime.datetime.strptime(data['shiftdate'], '%d-%m-%Y')
                data['shiftdate'] = output_date.strftime('%Y-%m-%d')
            else:
                data['shiftdate'] = ''
                
                
            getemployeeallotedshifturl = remoteURL+'users/api/getemployeeallotedshift'
            Request_ = requests.post(getemployeeallotedshifturl,headers=headers,data=data)
            response_data = Request_.json()
            return HttpResponse(json.dumps(response_data),content_type='application/json')
    else:
        return redirect('users:login')
    
def swapshift(request):
    
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data=request.POST.copy()
            
            if data['shiftdate1'] is not None and data['shiftdate1'] !='':
                output_date  = datetime.datetime.strptime(data['shiftdate1'], '%d-%m-%Y')
                data['shiftdate1'] = output_date.strftime('%Y-%m-%d')
            else:
                data['shiftdate1'] = ''
                
            if data['shiftdate2'] is not None and data['shiftdate2'] !='':
                output_date  = datetime.datetime.strptime(data['shiftdate2'], '%d-%m-%Y')
                data['shiftdate2'] = output_date.strftime('%Y-%m-%d')
            else:
                data['shiftdate2'] = ''
                
            swapshifturl = remoteURL+'users/api/swapshift'
            Request_ = requests.post(swapshifturl,headers=headers,data=data)
            response_data = Request_.json()
            return HttpResponse(json.dumps(response_data),content_type='application/json')
    else:
        return redirect('users:login')


def warningmail(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}
            data['mailType']=request.POST.get("mailtype")
            data['mailsubject']=request.POST.get("mailsubject")
            data['mailcontent']=request.POST.get("mailcontent")
            data['empid']=request.POST.get("empid")

            maildata=requests.post(sendwarningmailURL, data=data,headers=headers)
            mail_response = maildata.json()

        else:
            employee_list=requests.get(userListUrl, headers=headers)
            employee_list_response = employee_list.json()
            return render(request,'admin/Warningmail/warningmail.html',{'employeelist':employee_list_response['data']})
    else:
        return redirect('users:login')
    


def GetMailHistory(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}
            data['empid']=request.POST.get("employeeid")
           
            mailhistoryurl = remoteURL+'users/api/getmailhistorydata'
            Response_ = requests.post(mailhistoryurl,data=data,headers=headers)
            response_data = Response_.json()
            return HttpResponse(json.dumps(response_data),content_type='application/json')
    else:
        return redirect('users:login')
    


def apply_compoff(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 

    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}

        return render(request,'admin/compoff/apply_compoff.html')
    else:
        return redirect('users:login')
    



def get_compoffs(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}  
            status=request.POST.get('status')         
            get_compoffs_url = remoteURL+'users/api/get_user_'+status+'_compoff'
            get_compoffs_request = requests.post(get_compoffs_url,data=data,headers=headers)
            get_compoffs_response = get_compoffs_request.json()
            return HttpResponse(json.dumps(get_compoffs_response),content_type='application/json')
    else:
        return redirect('users:login')
    

def claim_compoff(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}  
            data['id']=request.POST.get('id')   
            data['claim_date']=request.POST.get('claim_date')         
            claim_compoff_url = remoteURL+'users/api/claim_compoff'
            claim_compoff_request = requests.post(claim_compoff_url,data=data,headers=headers)
            claim_compoff_response = claim_compoff_request.json()
            return HttpResponse(json.dumps(claim_compoff_response),content_type='application/json')
    else:
        return redirect('users:login')

def withdraw_compoff(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}  
            data['id']=request.POST.get('id')   
            withdraw_compoff_url = remoteURL+'users/api/withdraw_compoff'
            withdraw_compoff_request = requests.post(withdraw_compoff_url,data=data,headers=headers)
            withdraw_compoff_response = withdraw_compoff_request.json()
            return HttpResponse(json.dumps(withdraw_compoff_response),content_type='application/json')
    else:
        return redirect('users:login')


def change_claim_compoff_date(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}  
            data['id']=request.POST.get('id')   
            data['claim_date']=request.POST.get('claim_date')         
            change_claim_compoff_date_url = remoteURL+'users/api/change_claim_compoff_date'
            change_claim_compoff_date_request = requests.post(change_claim_compoff_date_url,data=data,headers=headers)
            change_claim_compoff_date_response = change_claim_compoff_date_request.json()
            return HttpResponse(json.dumps(change_claim_compoff_date_response),content_type='application/json')
    else:
        return redirect('users:login')

def get_compoff_requests(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}  
            status=request.POST.get('status')         
            get_compoffs_url = remoteURL+'users/api/get_manager_'+status+'_compoff_requests'
            get_compoffs_request = requests.post(get_compoffs_url,data=data,headers=headers)
            get_compoffs_response = get_compoffs_request.json()
            return HttpResponse(json.dumps(get_compoffs_response),content_type='application/json')
    else:
        return redirect('users:login')

def approve_compoff(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}  
            data['id']=request.POST.get('id')         
            approve_compoffs_url = remoteURL+'users/api/approve_compoff_requests'
            approve_compoffs_request = requests.post(approve_compoffs_url,data=data,headers=headers)
            approve_compoffs_response = approve_compoffs_request.json()
            return HttpResponse(json.dumps(approve_compoffs_response),content_type='application/json')
    else:
        return redirect('users:login')

def reject_compoff(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}  
            data['id']=request.POST.get('id')         
            data['reason']=request.POST.get('reason')         
            reject_compoffs_url = remoteURL+'users/api/reject_compoff_requests'
            reject_compoffs_request = requests.post(reject_compoffs_url,data=data,headers=headers)
            reject_compoffs_response = reject_compoffs_request.json()
            return HttpResponse(json.dumps(reject_compoffs_response),content_type='application/json')
    else:
        return redirect('users:login')
    
def reschedule_compoff(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}  
            data['id']=request.POST.get('id')         
            data['reason']=request.POST.get('reason')         
            reschedule_compoffs_url = remoteURL+'users/api/reschedule_compoff_requests'
            reschedule_compoffs_request = requests.post(reschedule_compoffs_url,data=data,headers=headers)
            reschedule_compoffs_response = reschedule_compoffs_request.json()
            return HttpResponse(json.dumps(reschedule_compoffs_response),content_type='application/json')
    else:
        return redirect('users:login')

def compoff_requests(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 

    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        return render(request,'admin/compoff/compoff_requests.html')
    else:
        return redirect('users:login')


def get_applications_requests(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data=request.POST.copy()
            status=request.POST.get('status')
            get_applications_url = remoteURL+'leave/api/get_manager_'+status+'_applications_requests'
            get_applications_request = requests.post(get_applications_url,data=data,headers=headers)
            get_applications_response = get_applications_request.json()
            return HttpResponse(json.dumps(get_applications_response),content_type='application/json')
    else:
        return redirect('users:login')

def excellatemarkreport(request):
    print("helloooooo")
    if request.session.get('PasswordChanged')==False:
        return redirect('users:updatepassword',id=request.session.get('userID'))
    tok = request.session.get('token',False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method=="POST":
            data={}
            data['start_date'] = request.POST.get("start_date")
            data['end_date'] = request.POST.get("end_date")
            data['empId'] = request.POST.get("empId")
            get_pagination_request_url = excellatemarkreporturl
            get_pagination_request=requests.post(get_pagination_request_url,data=data,headers=headers)
            get_pagination_response=get_pagination_request.json()
            return HttpResponse(json.dumps(get_pagination_response),content_type="application/json")
    else:
        return redirect('users:login')

