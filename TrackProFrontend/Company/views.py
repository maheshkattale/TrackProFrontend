from django.shortcuts import render,redirect
from django.contrib import messages
from helpers.static_info import *
import requests
from django.http.response import HttpResponse,HttpResponseRedirect
import json
from Users.views import accessToPage,accessDenied

BillingPeriodlistUrl = remoteURL + 'company/api/billingPeriodlist'
BillingPeriodbyidUrl = remoteURL + 'company/api/billingPeriodbyid'
addcompanydataURL = remoteURL+"company/api/addcompanyAPI"
getcompanydatalistURL = remoteURL+"company/api/companylist"
getcompanydataidURL= remoteURL+"company/api/companybyid"
updatecompanydataURL = remoteURL+"company/api/companybyidupdate"
deletecompanydataidURL =  remoteURL+"company/api/deletecompanyAPI"
companyListURL = remoteURL + "company/api/companytypelist"
deletecompanytypedataidURL = remoteURL + "company/api/delete_company_type"
companyByidURL = remoteURL + "company/api/companybyid"
companyupdateURL = remoteURL + "company/api/companybyidupdate"
companyleadsURL = remoteURL + "company/api/companyleadlist"
companypaymentlogURL = remoteURL + "company/api/companypaymentloglist"
makecompanypaymentURL = remoteURL + "company/api/addcompanypayment"
addplanURL = remoteURL + "company/api/addBillingPeriod"
updateplanperiodURL = remoteURL + "company/api/updateplanperiod"
getBillingPeriodbyidURL = remoteURL + "company/api/billingPerioddetails"
companyTypeListURL = remoteURL + "company/api/companytypelist"
addcompanyTypeListURL = remoteURL + "company/api/addCompanytype"
updateCompanyTypeListURL = remoteURL + "company/api/updateCompanyType"
particularcompanypaymentlogURL = remoteURL + "company/api/particualrcompanypaymentlog"
reminderListURL = remoteURL + "company/api/remindercompanylist"
sendreminderURL = remoteURL + "company/api/sendremindermail"
designationDataUrl = remoteURL + "company/api/designationfileapi"
departmentDataUrl = remoteURL + "company/api/departmentfileapi"
locationDataUrl = remoteURL + "company/api/locationfileapi"
uploadEmployeeExcel = remoteURL + "company/api/excel-employee"
dataruleslistURL = remoteURL+"rules/dataruleslist"
leaverulesURL = remoteURL+"rules/LeaveRules"
attruleURL = remoteURL+"rules/AttendanceRules"
trackproruleURL = remoteURL+"rules/TrackProRules"
add_announcement_url = remoteURL+"rules/addannouncement"
announcement_list_url = remoteURL+"rules/announcementlist"
announcement_delete_url = remoteURL+"rules/deleteannouncement"
add_news_url = remoteURL+"rules/addnews"
news_list_url = remoteURL+"rules/newslist"
news_delete_url = remoteURL+"rules/deletenews"
# Create your views here.


rolelistUrl = remoteURL + 'users/api/rolelist'
roleaddUrl = remoteURL + 'users/api/addrole'
updateroleURL = remoteURL + "users/api/updaterole"

userblockurl = remoteURL + "users/api/userblock"
userunblockurl = remoteURL + "users/api/userunblock"




def getcompanylist(request):
    tok = request.session.get('token', False)
    if tok:
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        # get token
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        access = accessToPage(Menu, url)
        if access == False:
            return redirect('users:accessDenied')
        data = {}
        files = {}
        if request.method == "POST":
            data['companyname'] = request.POST.get('companyname')
            data['caddress']= request.POST.get('caddress')
            data['contact']= request.POST.get('Contact')
            data['gstNumber']=request.POST.get('gstNumber')
            data['adhaarNumber']=request.POST.get('adhaarNumber')
            data['panNumber']=request.POST.get('panNumber')
            data['memberadmin']=request.POST.get('memberadmin')
            data['period']=request.POST.get('period')
            data['payment']=request.POST.get('payment')
            files['companylogos'] = request.FILES.get('companylogos')
            files['gstcertificate'] = request.FILES.get('gstcertificate')
            data['companyType'] = request.POST.get('companyType')

            empdata = requests.post(addcompanydataURL,data=data,files=files,headers=headers) 
            empiddata = empdata.json()
            if empiddata['response']['n'] == 1:
                messages.success(request,empiddata['response']['msg'])
                return redirect ('company:getcompanylist')
            else:
                messages.error(request,empiddata['response']['msg'])
                return redirect ('company:getcompanylist')    
        else:
            empdata = requests.get(getcompanydatalistURL,headers=headers) 
            empiddata = empdata.json()
            periodlistResponse = requests.get(BillingPeriodlistUrl, headers=headers)
            periodlistData = periodlistResponse.json()
            companyTypeResponse = requests.get(companyListURL, headers=headers)
            companyTypeData = companyTypeResponse.json()
      
            return render (request,'superadmin/companymaster/companylist.html',{'companylistdata':empiddata['data'],'periodlist':periodlistData['data'],'companytypelist':companyTypeData['data']})
    else:
        return redirect('users:login')

def BillingPeriodbyid(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data ={}
        data ['period'] = request.POST.get('period')
        periodbyIdResponse = requests.post(BillingPeriodbyidUrl, headers=headers,data=data)
        periodByIdData = periodbyIdResponse.json()
        return HttpResponse(json.dumps({'data': periodByIdData}), content_type="application/json")
    else:
        return redirect('users:login')

def CompanyById(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data = {}
        files = {}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        if request.method == "POST":
            data['id'] = id
            data['companyname'] = request.POST.get('companyname')
            data['caddress']= request.POST.get('caddress')
            data['contact']= request.POST.get('Contact')
            data['gstNumber']=request.POST.get('gstNumber')
            data['adhaarNumber']=request.POST.get('adhaarNumber')
            data['panNumber']=request.POST.get('panNumber')
            data['memberadmin']=request.POST.get('memberadmin')
            data['period']=request.POST.get('period')
            data['payment']=request.POST.get('payment')
            data['companyType'] = request.POST.get('companyType')
     
            empdata = requests.post(companyupdateURL,files=request.FILES,data=data,headers=headers) 
            empiddata = empdata.json()
            if empiddata['response']['n'] == 1:
                messages.success(request,empiddata['response']['msg'])
            else:
                messages.error(request,empiddata['response']['msg'])

            return HttpResponse(json.dumps({'data': empiddata}), content_type="application/json")
        else: 
            getdata = {}
            getdata['id'] = id
            periodlistResponse = requests.get(BillingPeriodlistUrl, headers=headers)
            periodlistData = periodlistResponse.json()
            companyTypeResponse = requests.get(companyListURL, headers=headers)
            companyTypeData = companyTypeResponse.json()
            companyInfoResponse = requests.post(companyByidURL, headers=headers,data=getdata)
            companyByidinfo = companyInfoResponse.json()
            return render(request, 'superadmin/companymaster/updatecompany.html',{'periodlist':periodlistData['data'],'companytypelist':companyTypeData['data'],'companyInfo':companyByidinfo['data']})
    else:
        return redirect('users:login')


def companyleads(request):
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
        companyLeadResponse = requests.get(companyleadsURL, headers=headers)
        companyLeadinfo = companyLeadResponse.json()
        
        companyTypeResponse = requests.get(companyListURL, headers=headers)
        companyTypeData = companyTypeResponse.json()
        periodlistResponse = requests.get(BillingPeriodlistUrl, headers=headers)
        periodlistData = periodlistResponse.json()
        return render(request, 'superadmin/companydetails/leads.html',{'periodlist':periodlistData['data'],'incompleteregistration':companyLeadinfo['incomplete'],'activecompany':companyLeadinfo['active'],'inactivecompany':companyLeadinfo['inactive'],'companytypelist':companyTypeData['data']})
    else:
        return redirect('users:login')

def comapanypaymenthistory(request):
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
        data={}
        if request.method == "POST":
            data['companyId'] = request.POST.get('companyId')
            data['planperiod']= request.POST.get('planperiod')
            data['payment']= request.POST.get('payment')
            paydata = requests.post(makecompanypaymentURL,data=data,headers=headers) 
            paymentlogdata = paydata.json()
            if paymentlogdata['response']['n'] == 1:
                messages.success(request,paymentlogdata['response']['msg'])
                return redirect ('company:comapanypaymenthistory')
            else:
                messages.error(request,paymentlogdata['response']['msg'])
                return redirect ('company:comapanypaymenthistory') 

        else:
            periodlistResponse = requests.get(BillingPeriodlistUrl, headers=headers)
            periodlistData = periodlistResponse.json()
            companylogResponse = requests.get(companypaymentlogURL, headers=headers)
            companyloginfo = companylogResponse.json()
            # companylogResponse = requests.get(companypaymentlogURL, headers=headers)
            # companyloginfo = companylogResponse.json()
        return render(request, 'superadmin/companydetails/payment_history.html',{'periodlist':periodlistData['data'],'companylist':companyloginfo['companylist'],'companypaymentlist':companyloginfo['companypaymentlist']}) 
    else:
        return redirect('users:login')



def planlist(request):
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
        if request.method == "POST":
            data = {}
            data['period'] = request.POST.get('period')
            data['amount'] = request.POST.get('amount')
            data['duration'] = request.POST.get('duration')
            plandata = requests.post(addplanURL,data=data,headers=headers) 
            planperioddata = plandata.json()
            if planperioddata['response']['n'] == 1:
                messages.success(request,planperioddata['response']['msg'])
                return redirect ('company:planlist')
            else:
                messages.error(request,planperioddata['response']['msg'])
                return redirect ('company:planlist') 
        else:
            periodlistResponse = requests.get(BillingPeriodlistUrl, headers=headers)
            periodlistData = periodlistResponse.json()
            return render(request, 'superadmin/planmaster/planlist.html',{'periodlist':periodlistData['data']})
    else:
        return redirect('users:login')



def updatePlan(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        data = {}
        data['id'] = id
        data['period'] = request.POST.get('period')
        data['amount'] = request.POST.get('amount')
        data['duration'] = request.POST.get('duration')
        plandata = requests.post(updateplanperiodURL,data=data,headers=headers) 
        planperioddata = plandata.json()
        if planperioddata['response']['n'] == 1:
            messages.success(request,planperioddata['response']['msg'])
        else:
            messages.error(request,planperioddata['response']['msg'])
        return HttpResponse(json.dumps({'data': planperioddata}), content_type="application/json")
    else:
        return redirect('users:login')    

def companyType(request):
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
            companytypelistResponse = requests.get(companyTypeListURL, headers=headers)
            companytypelistData = companytypelistResponse.json()
            return render(request, 'superadmin/companytype/companytype.html',{'companytypelistData':companytypelistData['data']})
        else:
            data = {}
            data['companyType'] = request.POST.get('companyType')
            companytypedata = requests.post(addcompanyTypeListURL,data=data,headers=headers) 
            companytypedatadata = companytypedata.json()
            if companytypedatadata['response']['n'] == 1:
                messages.success(request,companytypedatadata['response']['msg'])
                return redirect ('company:companyType')
            else:
                messages.error(request,companytypedatadata['response']['msg'])
                return redirect ('company:companyType')
    else:
        return redirect('users:login')
     

def updateCompanyType(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        data ={}
        data['id'] = request.POST.get('id')
        data ['companyType'] = request.POST.get('companyType')
        updatecompanyTypeResponse = requests.post(updateCompanyTypeListURL, headers=headers,data=data)
        updatecompanyTypeData = updatecompanyTypeResponse.json()
        if updatecompanyTypeData['response']['n'] == 1 :
            messages.success(request,updatecompanyTypeData['response']['msg'])
        else:
            messages.error(request,updatecompanyTypeData['response']['msg'])
        return HttpResponse(json.dumps({'data': updatecompanyTypeData}), content_type="application/json")
    else:
        return redirect('users:login')



def viewCompany(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        getdata = {}
        getdata['id'] = id
        periodlistResponse = requests.get(BillingPeriodlistUrl, headers=headers)
        periodlistData = periodlistResponse.json()
        companyTypeResponse = requests.get(companyListURL, headers=headers)
        companyTypeData = companyTypeResponse.json()
        companyInfoResponse = requests.post(companyByidURL, headers=headers,data=getdata)
        companyByidinfo = companyInfoResponse.json()
        companypaymentlogstr = particularcompanypaymentlogURL + "?companyId=" + str(id)
        companypaymentlogResponse = requests.get(companypaymentlogstr, headers=headers)
        companypaymentloginfo = companypaymentlogResponse.json()
        return render(request, 'superadmin/companymaster/viewcompany.html',{'periodlist':periodlistData['data'],'companytypelist':companyTypeData['data'],'companyInfo':companyByidinfo['data'],'paymenthistory':companypaymentloginfo['data']})
    else:
        return redirect('users:login')

def reminder(request):
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
        reminderListResponse = requests.get(reminderListURL, headers=headers)
        reminderListData = reminderListResponse.json()
        return render(request, 'superadmin/companydetails/reminder.html',{'incompletereminder':reminderListData['reminderincompleteList'],'activereminderlist':reminderListData['reminderactiveList'],'inactivereminderlist':reminderListData['reminderInactiveList']})
    else:
        return redirect('users:login')

def sendReminder(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data ={}
        companyId = request.POST.get('companyId')
        data ['companyId'] = request.POST.get('companyId')
        sendReminderResponse = requests.post(sendreminderURL, headers=headers,data=data)
        sendReminderData = sendReminderResponse.json()
        if sendReminderData['response']['n'] == 1 :
            messages.success(request,sendReminderData['response']['msg'])
        else:
            messages.error(request,sendReminderData['response']['msg'])
        return HttpResponse(json.dumps({'data': sendReminderData}), content_type="application/json")
    else:
        return redirect('users:login')

def companyrule(request):
    return render(request,'admin/companyrolemaster/addmaster.html')

def updatemasters(request):
    return render(request,'admin/companyrolemaster/addmastersmenu.html')



def designationmaster(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        file = request.FILES['file']
        filedata = requests.post(designationDataUrl,files=request.FILES,headers=headers)
        fileinfo = filedata.json()
        return HttpResponse(json.dumps(fileinfo),content_type='application/json')
    else:
        return redirect('users:login')



def departmentfiledata(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        file = request.FILES['file']
        depfiledata = requests.post(departmentDataUrl,files=request.FILES,headers=headers)
        depfileinfo = depfiledata.json()
        return HttpResponse(json.dumps(depfileinfo),content_type='application/json')
    else:
        return redirect('users:login')



def locationfiledata(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        file = request.FILES['file']
        projfiledata = requests.post(locationDataUrl,files=request.FILES,headers=headers)
        projfileinfo = projfiledata.json()
        return HttpResponse(json.dumps(projfileinfo),content_type='application/json')
    else:
        return redirect('users:login')



def addEmployeeExcel(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        employeefile = request.FILES.get('employeefile')
        filedata = requests.post(uploadEmployeeExcel,files=request.FILES,headers=headers)
        fileinfo = filedata.json()
        return HttpResponse(json.dumps(fileinfo),content_type='application/json')
    else:
        return redirect('users:login')



def addrules(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        id=request.session.get('userID')
        rules = requests.get(dataruleslistURL,headers=headers)
        rulesdata = rules.json()
        leverageslist = [1,2,3,4,5,6,7,8,9,10]
        leaverules =  rulesdata['leavedata']
        attrules =  rulesdata['attdata']
        trackprorules =  rulesdata['trackprodata']
        data = {}
        if trackprorules != []:
            data={
                trackprorules[0]['color']:trackprorules[0]['points'],
                trackprorules[1]['color']:trackprorules[1]['points'],
                trackprorules[2]['color']:trackprorules[2]['points'],
                trackprorules[3]['color']:trackprorules[3]['points'],
                trackprorules[4]['color']:trackprorules[4]['points'],
                trackprorules[5]['color']:trackprorules[5]['points'],
                trackprorules[6]['color']:trackprorules[6]['points'],
                trackprorules[7]['color']:trackprorules[7]['points'],
            }
        
        return render (request,'admin/companyrolemaster/rulesmanagement.html',{'token':t,'userid':id,'leaverules':leaverules,'attrules':attrules,'trackprorules':data,'levglist':leverageslist})
    else:
        return redirect('users:login')

def updaterules(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        id=request.session.get('userID')
        rules = requests.get(dataruleslistURL,headers=headers)
        rulesdata = rules.json()
        leverageslist = [1,2,3,4,5,6,7,8,9,10]
        leaverules =  rulesdata['leavedata']
        attrules =  rulesdata['attdata']
        trackprorules =  rulesdata['trackprodata']
        data = {}
        if trackprorules != []:
            data={
                trackprorules[0]['color']:trackprorules[0]['points'],
                trackprorules[1]['color']:trackprorules[1]['points'],
                trackprorules[2]['color']:trackprorules[2]['points'],
                trackprorules[3]['color']:trackprorules[3]['points'],
                trackprorules[4]['color']:trackprorules[4]['points'],
                trackprorules[5]['color']:trackprorules[5]['points'],
                trackprorules[6]['color']:trackprorules[6]['points'],
                trackprorules[7]['color']:trackprorules[7]['points'],
            }

        return render (request,'admin/companyrolemaster/updaterules.html',{'token':t,'userid':id,'leaverules':leaverules,'attrules':attrules,'trackprorules':data,'levglist':leverageslist})
    else:
        return redirect('users:login')



def fleaverule(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        leaverules = requests.post(leaverulesURL,data=request.POST,headers=headers)
        rulesdata = leaverules.json()
        return HttpResponse(json.dumps(rulesdata))
    else:
        return redirect('users:login')


def fattrule(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        ATTrules = requests.post(attruleURL,data=request.POST,headers=headers)
        attrulesdata = ATTrules.json()
        return HttpResponse(json.dumps(attrulesdata))
    else:
        return redirect('users:login')


def ftrackprorule(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        trackprorules = requests.post(trackproruleURL,data=request.POST,headers=headers)
        trackprorulesdata = trackprorules.json()
        return HttpResponse(json.dumps(trackprorulesdata))
    else:
        return redirect('users:login')

def anouncement(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}
            data['announcementText'] = request.POST.get('announcement')
            data['date'] = request.POST.get('date')
            add_announcement_request = requests.post(add_announcement_url,data=data,headers=headers)
            add_announcement_response = add_announcement_request.json()
            if add_announcement_response['response']['n'] == 1:
                return redirect('company:anouncement')
            else:
                return render(request,'admin/companyrolemaster/anunoncement.html')
        announcement_list_request = requests.get(announcement_list_url,headers=headers)
        announcement_list_response = announcement_list_request.json()
        return render(request,'admin/companyrolemaster/anunoncement.html',{'announcementlist':announcement_list_response['data']})
    else:
        return redirect('users:login')

def deleteanouncement(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['id'] = id
        announcement_delete_request = requests.get(announcement_delete_url,params=data,headers=headers)
        announcement_delete_response = announcement_delete_request.json()
        if announcement_delete_response['response']['n'] == 1:
            return redirect('company:anouncement')
    else:
        return redirect('users:login')
    

def news(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}
            data['newsText'] = request.POST.get('news')
            data['date'] = request.POST.get('date')
            add_news_request = requests.post(add_news_url,data=data,headers=headers)
            add_news_response = add_news_request.json()
            if add_news_response['response']['n'] == 1:
                return redirect('company:news')
            else:
                return render(request,'admin/companyrolemaster/news.html')
        news_list_request = requests.get(news_list_url,headers=headers)
        news_list_response = news_list_request.json()
        return render(request,'admin/companyrolemaster/news.html',{'newslist':news_list_response['data']})
    else:
        return redirect('users:login')


def deletenews(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['id'] = id
        news_delete_request = requests.get(news_delete_url,params=data,headers=headers)
        news_delete_response = news_delete_request.json()
        if news_delete_response['response']['n'] == 1:
            return redirect('company:news')
    else:
        return redirect('users:login')
   


    
def delete_company(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['id']=id
        delete_request = requests.post(deletecompanydataidURL, headers=headers,data=data)
        delete_response = delete_request.json()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('users:login')



def delete_company_type(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['id']=id
        delete_request = requests.post(deletecompanytypedataidURL, headers=headers,data=data)
        delete_response = delete_request.json()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('users:login')



def userblock(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['userID']=id
        block_request = requests.get(userblockurl, headers=headers,data=data)
        block_response = block_request.json()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('users:login')




def userunblock(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['userID']=id
        unblock_request = requests.get(userunblockurl, headers=headers,data=data)
        unblock_response = unblock_request.json()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('users:login')