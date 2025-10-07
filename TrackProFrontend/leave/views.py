from django.shortcuts import render,redirect
from django.contrib import messages
from helpers.static_info import *
import requests
from django.http.response import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from Users.views import accessToPage,accessDenied,checksession
from leave.templatetags.encryption_filters import decrypt_parameter
from helpers.static_info import *

userListUrl = remoteURL + "users/api/userlist"
user_emp_list_url = remoteURL + "users/api/user_emp_list"
leave_user_emp_list_url = remoteURL + "leave/api/leave_user_emp_list"
departmentUrl = remoteURL + "department/api/departmentlist"
get_per_date_leaves_count_url= remoteURL + "leave/api/get_per_date_leaves_count"
#leave
apply_leave_Url = remoteURL + "leave/api/apply_leave_api"
filter_leavemaning_emp=remoteURL+'leave/api/leave_mapping_emp_filter'
Apply_Leave_MappingUrl=remoteURL+'leave/api/Apply_Leave_Mapping'
leaveUrl=remoteURL+"leave/api/leaveapi"
FilterleaveListAPIUrl=remoteURL+"leave/api/FilterleaveListAPI"
leaveactionAPIUrl=remoteURL+"leave/api/leaveactionAPI"
get_filter_leavesurl=remoteURL+"leave/api/get_filter_leaves"
leavelisturl = remoteURL+"leave/api/leaveListAPI"
userleavelisturl = remoteURL+"leave/api/UserleaveListAPI"
withdraw_application_url = remoteURL+"leave/api/withdraw_application"
leavedeleteurl = remoteURL+"leave/api/deleteleaveAPI"
getbyidleaveurl = remoteURL+"leave/api/getbyidleaveAPI"
updateleaveurl = remoteURL+"leave/api/updatebyidleaveAPI"
updatedraftleaveurl = remoteURL+"leave/api/updatedrafyleaveAPI"
statusleaveurl = remoteURL+"leave/api/statusleaveAPI"
leavemappingdataURL =  remoteURL+"leave/api/leavemappingAPI"
leavemappinglistAPIURL = remoteURL+"leave/api/leavemappinglistAPI"
leaverequestURL = remoteURL+"leave/api/leaverequestAPI"
leaveactionURL =  remoteURL+"leave/api/leaveactionAPI"
adminLeaveApprovedURL = remoteURL+"leave/api/admin-leave-approved"
checkAttendanceDataURL= remoteURL+"users/api/checkAttendanceData"
leave_maped_managers_listurl=remoteURL+"leave/api/mapped_managers"
leave_calculation_url=remoteURL+"leave/api/leave_calculation"
filter_leavemaning_emp=remoteURL+'leave/api/leave_mapping_emp_filter'
user_emp_list_url = remoteURL + "users/api/user_emp_list"
employee_application_details_url = remoteURL + "leave/api/employee_application_details"
get_past_application_url = remoteURL + "leave/api/get_past_application"
leavetypeUrl=remoteURL+'leave/api/get_leave_type_list'
leavetypeaddUrl=remoteURL+'leave/api/add_leave_type'
deleteleavetypeURL=remoteURL+'leave/api/delete_leave_type'
updateleavetypeURL=remoteURL+'leave/api/update_leave_type'

@csrf_exempt
def leavemappingOnchangeAjax(request):
    tok = request.session['token']
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            Managerid = request.POST.get('id', None)

            updateleaveMappingUrl = remoteURL + \
                'leave/api/leavemappingJoinQuery?managerId={}'.format(Managerid)
            Mapp = requests.get(updateleaveMappingUrl, headers=headers)
            if Mapp:
                mappings = Mapp.json()
                return HttpResponse(json.dumps(mappings), content_type="application/json")
            else:
                return HttpResponse(json.dumps({'n': 0, 'Msg': 'Json object not serialized', 'Status': 'Failed'}), content_type="application/json")
    else:
        return redirect('users:login')


def leavemapping(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        access = accessToPage(Menu, url)
        if access == False:
            return redirect('users:accessDenied')
        data={}
        
        data['UserId'] = request.session['userID']
        context={}
        
        return render(request,'admin/leave/leavemapping.html',context)
    else:
        return redirect('users:login')  

def get_leavemapping_employee_list(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}

        data={}
        
        data['UserId'] = request.session['userID']
        employeeListRequest = requests.get(leave_user_emp_list_url,headers=headers)
        employeeList = employeeListRequest.json()
        context={'data':employeeList['data']}
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        context={'data':'login required'}
        return HttpResponse(json.dumps(context), content_type="application/json")



def leave_mapping_emp_filter(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['UserId'] = request.session['userID']
        data['department'] =  request.POST.get('department')
        data['name'] = request.POST.get('name')

        
        filter_employee = requests.post(filter_leavemaning_emp,data=data,headers=headers)
        filter_employee_response = filter_employee.json()
        employeeListRequest = requests.get(user_emp_list_url,headers=headers)
        employeeList = employeeListRequest.json()
            
        return HttpResponse(json.dumps({"filter_employees":filter_employee_response['data'],"managers":employeeList['data']}), content_type="application/json")
    else:
        return redirect('users:login')



def updateleavemapping(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        data = {}
        data['employeeId'] =  request.POST.getlist('employeeID')
        managerId = request.POST.get('managerId')
        data['managerids'] = json.loads(managerId)
        userlist = requests.post(leavemappingdataURL,data=data,headers=headers)
        userdata = userlist.json()
        if userdata['response']['n'] == 1 :
            messages.success(request,userdata['response']['msg'])
        else:
            messages.error(request,userdata['response']['msg'])
        return HttpResponse(json.dumps({'data': userdata}), content_type="application/json")
    else:
        return redirect('users:login') 
    
@csrf_exempt
def applyleave(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        access = accessToPage(Menu, url)
        if access == False:
            return redirect('users:accessDenied')

        if request.method == "POST":
            data={}
            data['UserId'] = request.session['userID']           
            data['leavetype'] = request.POST.get('leavetype')         
            data['leave_status'] = request.POST.get('leavestatus')  
            data['start_date'] = request.POST.get('start_date') 
            data['end_date'] = request.POST.get('end_date')      
            data['leave_duration'] = request.POST.get('duration')           
            data['reason'] = request.POST.get('reason')    
            data['WorkFromHome'] = request.POST.get('WFH')    

            response1 = requests.post(leaveUrl,data=data,headers=headers,files=request.FILES)          
            leavedata = response1.json()
            if leavedata['response']['n'] == 1 :
                return HttpResponse(json.dumps(leavedata),content_type='application/json')
            else:
                return HttpResponse(json.dumps(leavedata),content_type='application/json')

        else:
            user_leaves = requests.get(userleavelisturl,headers=headers)
            leave_data = user_leaves.json()
            managermapedlist = requests.get(leave_maped_managers_listurl,headers=headers)
            maped_managers = managermapedlist.json()
            leavetypesrequest = requests.get(leavetypeUrl,headers=headers)
            leavetypesresponse = leavetypesrequest.json()
            return render(request,'admin/leave/leave.html',{"Withdraw_list":leave_data['data']['Withdraw_list'],"Rejected_list":leave_data['data']['Rejected_list'],"Approved_list":leave_data['data']['Approved_list'],"pending_list":leave_data['data']['pending_list'],"Draft_list":leave_data['data']['Draft_list'],"Draft_list":leave_data['data']['Draft_list'],"managerlist":maped_managers['data'],
                                                            'leavetypes':leavetypesresponse['data']})
    else:
        return redirect('users:login') 


@csrf_exempt
def apply_leave_front(request):

    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        if request.method == "POST":
            data=request.POST.copy()
            applyleave_request = requests.post(apply_leave_Url,data=data,headers=headers,files=request.FILES)          
            apply_leave_response = applyleave_request.json()
            return HttpResponse(json.dumps(apply_leave_response),content_type='application/json')
        else:
            return HttpResponse(json.dumps({"data":{},"response":{"n" : 0,"msg" :"method not allowed","status" : "warning"}}),content_type='application/json')
    else:
        return HttpResponse(json.dumps({"data":{},"response":{"n" : 0,"msg" :"session expired","status" : "warning"}}),content_type='application/json')



def updateapplyleave(request,id):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        data={}
        if request.method == 'POST':   
            start_date = request.POST.get('start_date') 
            splitstart_date = start_date.split('-')
            

            end_date = request.POST.get('end_date') 
            splitend_date = end_date.split('-')
            

            if len(splitstart_date[0]) > 3 :
                data['start_date'] = request.POST.get('start_date')
            else:
                splitstart_datestr = '-'.join(reversed(splitstart_date))
                data['start_date'] = splitstart_datestr

            if len(splitend_date[0]) > 3 :
                data['end_date'] = request.POST.get('end_date')
            else:
                splitend_datestr = '-'.join(reversed(splitend_date))
                data['end_date'] = splitend_datestr
                     
            data['reason'] = request.POST.get('reason') 
            data['leavetype']=  request.POST.get('leavetype') 
            data['leavestatus']=  request.POST.get('leavestatus') 
            data['leaveduration']=  request.POST.get('leaveduration') 
                 
            response1 = requests.post(updatedraftleaveurl+"/{}".format(id),data=data,headers=headers,files=request.FILES)
            leavedata = response1.json()


            return HttpResponse(json.dumps(leavedata),content_type='application/json')
    else:
        return redirect('users:login')      
            

    

def updateleave(request,id):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        
        data={}
        if request.method == 'POST':   
            start_date = request.POST.get('start_date') 
            splitstart_date = start_date.split('-')
            

            end_date = request.POST.get('end_date') 
            splitend_date = end_date.split('-')
            

            if len(splitstart_date[0]) > 3 :
                data['start_date'] = request.POST.get('start_date')
            else:
                splitstart_datestr = '-'.join(reversed(splitstart_date))
                data['start_date'] = splitstart_datestr

            if len(splitend_date[0]) > 3 :
                data['end_date'] = request.POST.get('end_date')
            else:
                splitend_datestr = '-'.join(reversed(splitend_date))
                data['end_date'] = splitend_datestr
                     
            data['reason'] = request.POST.get('reason') 
            data['leavetype'] = request.POST.get('leavetype')             
            response1 = requests.post(updateleaveurl+"/{}".format(id),data=data,headers=headers,files=request.FILES)
            leavedata = response1.json()
            return HttpResponse(json.dumps(leavedata),content_type='application/json')

        response1 = requests.get(getbyidleaveurl+"/{}".format(id),data=data,headers=headers)
        leavedata = response1.json()
        return HttpResponse(json.dumps(leavedata),content_type='application/json')
    else:
        return redirect('users:login') 

def statustypeleave(request,id):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        Menu = request.session['Menu']
       
        data={}
        if request.method == "GET":
            data['id']=id
            userlist = requests.post(statusleaveurl,data=data,headers=headers)
            leave_data = userlist.json()
            if leave_data['response']['n'] == 1 :
                messages.success(request,leave_data['response']['msg'])
                return redirect('leave:applyleave') 
            else:
                messages.error(request,leave_data['response']['msg'])
                return redirect('leave:applyleave') 
    else:
        return redirect('users:login') 

def statustypeleaveajax(request,id):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
       
        data={}
        if request.method == "POST":
            data['id']=id
            userlist = requests.post(statusleaveurl,data=data,headers=headers)
            leave_data = userlist.json()
            return HttpResponse(json.dumps(leave_data),content_type='application/json')

    else:
        return redirect('users:login') 

def deleteleave(request,id):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        
        data={}
        if request.method == "GET":
            data['id']=id
            userlist = requests.post(leavedeleteurl,data=data,headers=headers)
            leave_data = userlist.json()
            if leave_data['response']['n'] == 1 :
                messages.success(request,leave_data['response']['msg'])
                return redirect('leave:applyleave') 
            else:
                messages.error(request,leave_data['response']['msg'])
                return redirect('leave:applyleave') 
    else:
        return redirect('users:login') 


def widhrawapplication(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        
        data={}
        if request.method == "POST":
            data['id']=request.POST.get('id')
            application_request = requests.post(withdraw_application_url,data=data,headers=headers)
            leave_data = application_request.json()
            return HttpResponse(json.dumps(leave_data),content_type='application/json')
    else:
        return redirect('users:login') 

def leaverequest(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 
    

    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        access = accessToPage(Menu, url)
        if access == False:
            return redirect('users:accessDenied')
    
        # userlist = requests.get(leaverequestURL,headers=headers)
        # userdata = userlist.json()
        # return render(request,'admin/leave/leaverequest.html',{'expiredlist':userdata['expiredlist'],'withdraw_list':userdata['withdrawlist'],'pending_list':userdata['pendinglist'],'Approved_list':userdata['approvedlist'],'Rejected_list':userdata['rejectedlist']})
        return render(request,'admin/leave/leaverequest.html')
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
        Menu = request.session['Menu']
        
        url = request.path
        access = accessToPage(Menu, url)
        if access == False:
            return redirect('users:accessDenied')
        if request.method == "POST":
            data={}
            data['UserId'] = request.session['userID']           
            data['leavetype'] = request.POST.get('leavetype')         
            data['leave_status'] = request.POST.get('leavestatus')  
            data['start_date'] = request.POST.get('start_date') 
            data['end_date'] = request.POST.get('end_date')      
            data['leave_duration'] = request.POST.get('duration')           
            data['reason'] = request.POST.get('reason')    
            data['WorkFromHome'] = request.POST.get('WFH')    
            response1 = requests.post(leaveUrl,data=data,headers=headers)          
            leavedata = response1.json()
            if leavedata['response']['n'] == 1 :
                return HttpResponse(json.dumps(leavedata),content_type='application/json')
            else:
                return HttpResponse(json.dumps(leavedata),content_type='application/json')

        else:
            # leavelist = requests.get(leavelisturl,headers=headers)
            # leave_data = leavelist.json()
            # managermapedlist = requests.get(leave_maped_managers_listurl,headers=headers)
            # maped_managers = managermapedlist.json()

            return render(request,'admin/leave/calender.html',{
                # "leave_data":leave_data['data'],
                # "managerlist":maped_managers['data'],
                "imageURL":imageURL
                })
    else:
        return redirect('users:login') 

def get_filter_leaves(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        Menu = request.session['Menu']
       
        if request.method == "POST":
            data={}
            data['searchdate'] = request.POST.get('searchdate')           
            response1 = requests.post(get_filter_leavesurl,data=data,headers=headers)          
            leavedata = response1.json()
            if leavedata['response']['n'] == 1 :
                return HttpResponse(json.dumps(leavedata),content_type='application/json')
            else:
                return HttpResponse(json.dumps(leavedata),content_type='application/json')
    else:
        return redirect('users:login')

def get_per_date_leaves_count(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        Menu = request.session['Menu']
       
        if request.method == "POST":
            data={}
            data['month'] = request.POST.get('month')           
            data['year'] = request.POST.get('year')           
            response1 = requests.post(get_per_date_leaves_count_url,data=data,headers=headers)          
            leavedata = response1.json()
            if leavedata['n'] == 1 :
                return HttpResponse(json.dumps(leavedata),content_type='application/json')
            else:
                return HttpResponse(json.dumps(leavedata),content_type='application/json')
    else:
        return redirect('users:login')

def leaveactionFront(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        if request.method == "POST":
            data={}
            data['id'] = request.POST.get('id')           
            data['comment'] = request.POST.get('comment')  
            # leaveactionAPIUrl=remoteURL+"users/api/leaveonlyactionAPI"

            response1 = requests.post(leaveactionAPIUrl,data=data,headers=headers)          
            leavedata = response1.json()
            return HttpResponse(json.dumps(leavedata),content_type='application/json')
    else:
        return redirect('users:login')
       
        
def reject_approved_application(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}
            data['id'] = request.POST.get('id')           
            data['comment'] = request.POST.get('comment')  
            reject_approved_application_Url=remoteURL+"leave/api/reject_approved_application"
            response1 = requests.post(reject_approved_application_Url,data=data,headers=headers)          
            leavedata = response1.json()
            return HttpResponse(json.dumps(leavedata),content_type='application/json')
    else:
        return redirect('users:login')
def approve_rejected_application(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}
            data['id'] = request.POST.get('id')           
            approve_rejected_application_Url=remoteURL+"leave/api/approve_rejected_application"
            response1 = requests.post(approve_rejected_application_Url,data=data,headers=headers)          
            leavedata = response1.json()
            return HttpResponse(json.dumps(leavedata),content_type='application/json')
    else:
        return redirect('users:login')

def FilterleaveListAPIfront(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        
        if request.method == "POST":
            data={}
            data['ApplicationType'] = request.POST.get('ApplicationType')        
            data['department_value'] = request.POST.get('department_value')        
            data['name'] = request.POST.get('name')        
            data['month'] = request.POST.get('month')        
            data['year'] = request.POST.get('year')        
            response1 = requests.post(FilterleaveListAPIUrl,data=data,headers=headers)          
            leavedata = response1.json()
            if leavedata['response']['n'] == 1 :
                return HttpResponse(json.dumps(leavedata),content_type='application/json')
            else:
                return HttpResponse(json.dumps(leavedata),content_type='application/json')
    else:
        return redirect('users:login')


def Apply_Leave_MappingFront(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        
        if request.method == "POST":
            data={}
            data['New_dictionary'] = request.POST.getlist('New_dictionary')      

            response1 = requests.post(Apply_Leave_MappingUrl,data=data,headers=headers)          
            leavedata = response1.json()
            if leavedata['response']['n'] == 1 :
                return HttpResponse(json.dumps(leavedata),content_type='application/json')
            else:
                return HttpResponse(json.dumps(leavedata),content_type='application/json')
    else:
        return redirect('users:login')
    



def leave_mapping_emp_filter(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['UserId'] = request.session['userID']
        data['department'] =  request.POST.get('department')
        data['name'] = request.POST.get('name')

        
        filter_employee = requests.post(filter_leavemaning_emp,data=data,headers=headers)
        filter_employee_response = filter_employee.json()
        employeeListRequest = requests.get(user_emp_list_url,headers=headers)
        employeeList = employeeListRequest.json()
            
        return HttpResponse(json.dumps({"filter_employees":filter_employee_response['data'],"managers":employeeList['data']}), content_type="application/json")
    else:
        return redirect('users:login')



def leavedetails(request,leaveid,manager_approvel_id):

    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login')
    leaveid = decrypt_parameter(leaveid)
    manager_approvel_id = decrypt_parameter(manager_approvel_id)

    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        data={}
        data['LeaveId'] = leaveid
        employee_application_details = requests.post(employee_application_details_url,data=data,headers=headers)
        employee_application_details_response = employee_application_details.json()
        userID = request.session.get('userID')
        
        return render(request,'admin/leave/leavedetails.html',{
                                                                "Login_Manager":str(userID),
                                                                "TrackPro_average_percentage":employee_application_details_response['data']['TrackPro_average_percentage'],
                                                                "TrackPro_Percentages_History":employee_application_details_response['data']['TrackPro_Percentages_History'],
                                                                "Past_Applications":employee_application_details_response['data']['Past_Applications'],
                                                                "manager_approvel_id":manager_approvel_id,
                                                                "application_details":employee_application_details_response['data']['currentleavedata'],
                                                                "managers_status":employee_application_details_response['data']['currentleavedata']['managers_status'],
                                                                "Application_Approval":employee_application_details_response['data']['Application_Approval'],
                                                                "approved_application_count":employee_application_details_response['data']['Approved_application_count'],
                                                                "pending_application_count":employee_application_details_response['data']['Pending_application_count'],
                                                                "withdraw_application_count":employee_application_details_response['data']['Withdraw_application_count'],
                                                                "rejected_application_count":employee_application_details_response['data']['Rejected_application_count'],
                                                                "total_application_count":employee_application_details_response['data']['Total_application_count'],
                                                               })
    else:
        return redirect('users:login') 



def past_leaves(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['UserId'] =  request.POST.get('UserId')
        data['leave_status'] = request.POST.get('leave_status')
        data['LeaveId'] = request.POST.get('LeaveId')

        
        get_past_application = requests.post(get_past_application_url,data=data,headers=headers)
        get_past_application_response = get_past_application.json()

            
        return HttpResponse(json.dumps({"Applications":get_past_application_response['data']['Applications']}), content_type="application/json")
    else:
        return redirect('users:login')
    


# views.py
from django.template import loader
from django.shortcuts import get_object_or_404

def leavedetails1(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}    
        leave_id = request.GET.get('leave_id')
        manager_approvel_id = request.GET.get('id')
        data={}
        data['LeaveId'] = leave_id
        employee_application_details = requests.post(employee_application_details_url,data=data,headers=headers)
        employee_application_details_response = employee_application_details.json()
        userID = request.session.get('userID')
    # Perform any necessary processing with leave_id and id
    # Load the HTML template with the data
    template = loader.get_template('admin/leave/leavedetails.html')
    context = {
                "Login_Manager":str(userID),
                "TrackPro_average_percentage":employee_application_details_response['data']['TrackPro_average_percentage'],
                "TrackPro_Percentages_History":employee_application_details_response['data']['TrackPro_Percentages_History'],
                "Past_Applications":employee_application_details_response['data']['Past_Applications'],
                "manager_approvel_id":manager_approvel_id,
                "application_details":employee_application_details_response['data']['currentleavedata'],
                "managers_status":employee_application_details_response['data']['currentleavedata']['managers_status'],
                "Application_Approval":employee_application_details_response['data']['Application_Approval'],
                "approved_application_count":employee_application_details_response['data']['Approved_application_count'],
                "pending_application_count":employee_application_details_response['data']['Pending_application_count'],
                "withdraw_application_count":employee_application_details_response['data']['Withdraw_application_count'],
                "rejected_application_count":employee_application_details_response['data']['Rejected_application_count'],
                "total_application_count":employee_application_details_response['data']['Total_application_count'],
                }
    

    rendered_html = template.render(context, request)

    # Return the HTML content as a response
    return HttpResponse(rendered_html)





def compoff_granted(request):
    if checksession(request):
        messages.error(request,'Session expired !')
        return redirect ('users:login') 
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    if tok:
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        # access = accessToPage(Menu, url)
        # if access == False:
        #     return redirect('users:accessDenied')
        data={}
        granted_compoff_list_url=remoteURL+"leave/api/granted_compoff_list"
        granted_compoff_list_request = requests.post(granted_compoff_list_url,data=data,headers=headers)
        granted_compoff_list_response = granted_compoff_list_request.json()
        
        
        data['UserId'] = request.session['userID']
        context= {
                    "AllCompOff": granted_compoff_list_response['AllCompoff'],
                    "ApprovedCompoff": granted_compoff_list_response['ApprovedCompoff'],
                    "RejectedCompoff": granted_compoff_list_response['RejectedCompoff'],
                    "ExpiredCompoff": granted_compoff_list_response['ExpiredCompoff'],
                }
        
        return render(request,'admin/compoff_master/compoff_approved.html',context)
    else:
        return redirect('users:login')  
    








def leavetype(request):
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
            leavetypereponse = requests.get(leavetypeUrl,headers=headers)   
            leavedata = leavetypereponse.json()
            print("leavedata",leavedata)
            return render(request, 'admin/leave/leavetype/leavetype.html',{'leavetypes':leavedata['data']})
        else:
            data = {}
            data['TypeName'] = request.POST.get('TypeName')
            leaveaddreponse = requests.post(leavetypeaddUrl,headers=headers,data=data)   
            leavedata = leaveaddreponse.json()
            if leavedata['response']['n'] == 1:
                messages.success(request,leavedata['response']['msg'])
                return redirect ('leave:leavetype')
            else:
                messages.error(request,leavedata['response']['msg'])
                return redirect ('leave:leavetype') 
    else:
        return redirect('users:login')
    

def delete_leavetype(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data ={}
    data['id'] = request.POST.get('id')
    delete_leavetypeResponse = requests.post(deleteleavetypeURL, headers=headers,data=data)
    delete_leavetypeData = delete_leavetypeResponse.json()
    print("delete_leavetypeData",delete_leavetypeData)
    if delete_leavetypeData['response']['n'] == 1 :
        messages.success(request,delete_leavetypeData['response']['msg'])
    else:
        messages.error(request,delete_leavetypeData['response']['msg'])
    return HttpResponse(json.dumps(delete_leavetypeData), content_type="application/json")


def update_leavetype(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data ={}
    data['id'] = request.POST.get('id')
    data ['TypeName'] = request.POST.get('TypeName')
    update_leavetypeResponse = requests.post(updateleavetypeURL, headers=headers,data=data)
    update_leavetypeData = update_leavetypeResponse.json()
    print("update_leavetypeData",update_leavetypeData)
    if update_leavetypeData['response']['n'] == 1 :
        messages.success(request,update_leavetypeData['response']['msg'])
    else:
        messages.error(request,update_leavetypeData['response']['msg'])
    return HttpResponse(json.dumps(update_leavetypeData), content_type="application/json")

def add_leavetype(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data ={}
    data ['TypeName'] = request.POST.get('TypeName')
    add_leavetypeResponse = requests.post(leavetypeaddUrl, headers=headers,data=data)
    add_leavetypeData = add_leavetypeResponse.json()
    print("add_leavetypeData",add_leavetypeData)

    return HttpResponse(json.dumps(add_leavetypeData), content_type="application/json")











