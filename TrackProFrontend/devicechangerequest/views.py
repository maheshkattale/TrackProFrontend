from django.shortcuts import render,redirect
from django.contrib import messages
from Users.views import remoteURL
import requests
from django.http.response import HttpResponse,HttpResponseRedirect
import json
from Users.views import accessToPage,accessDenied


devicechangerequestslistURL = remoteURL+"users/api/devicechangerequestslist"
pendingdevicechangerequestslistURL = remoteURL+"users/api/pendingdevicechangerequestslist"
approveddevicechangerequestslistURL = remoteURL+"users/api/approveddevicechangerequestslist"
rejecteddevicechangerequestslistURL = remoteURL+"users/api/rejecteddevicechangerequestslist"



def devicechangerequestlist(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        Menu = request.session['Menu']
        url = request.path
        access = accessToPage(Menu, url)
        if access == False:
            return redirect('users:accessDenied')
        
        devicechangerequest = requests.get(devicechangerequestslistURL, headers=headers)
        devicechangeresponse = devicechangerequest.json()
        
        pendingdevicechangerequest = requests.get(pendingdevicechangerequestslistURL, headers=headers)
        pendingdevicechangeresponse = pendingdevicechangerequest.json()

        approveddevicechangerequest = requests.get(approveddevicechangerequestslistURL, headers=headers)
        approveddevicechangeresponse = approveddevicechangerequest.json()

        rejecteddevicechangerequest = requests.get(rejecteddevicechangerequestslistURL, headers=headers)
        rejecteddevicechangeresponse = rejecteddevicechangerequest.json()

        context={
            'all_applications':devicechangeresponse['data'],
            'pending_applications':pendingdevicechangeresponse['data'],
            'approved_applications':approveddevicechangeresponse['data'],
            'rejected_applications':rejecteddevicechangeresponse['data'],
        }
        return render(request, 'admin/device_change_request/device_change_request_list.html',context)
    else:
        return redirect('users:login')
    

def approvedevicechangerequest(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}
            data['id'] = request.POST.get('id')           
            approvedevicechangerequestUrl=remoteURL+"users/api/approvedevicechangerequest"
            approvedevicechangerequest = requests.post(approvedevicechangerequestUrl,data=data,headers=headers)          
            approvedevicechangeresponse = approvedevicechangerequest.json()

            return HttpResponse(json.dumps(approvedevicechangeresponse),content_type='application/json')
    else:
        return redirect('users:login')
       
    

def rejectdevicechangerequest(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data={}
            data['id'] = request.POST.get('id')           
            data['rejection_reason'] = request.POST.get('rejection_reason') 
                      
            reject_devicechangerequestUrl=remoteURL+"users/api/reject_devicechangerequest"
            reject_devicechangerequest = requests.post(reject_devicechangerequestUrl,data=data,headers=headers)          
            reject_devicechangeresponse = reject_devicechangerequest.json()

            return HttpResponse(json.dumps(reject_devicechangeresponse),content_type='application/json')
    else:
        return redirect('users:login')
       
    