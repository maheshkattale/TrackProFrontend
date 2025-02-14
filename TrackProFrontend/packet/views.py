from django.shortcuts import render,redirect
from django.contrib import messages
from Users.views import remoteURL
import requests
from django.http.response import HttpResponse,HttpResponseRedirect
import json
from Users.views import accessToPage,accessDenied

packetlistUrl = remoteURL + 'packet/api/get_packet_list'
packetaddUrl = remoteURL + 'packet/api/add_packet'
deletepacketURL = remoteURL + 'packet/api/delete_packet'
updatepacketURL = remoteURL + "packet/api/update_packet"
menuitemlistURL = remoteURL + "users/api/menuitem"
addPermissionURL = remoteURL + "users/api/addpermission"
getPermissionURL = remoteURL + "users/api/getPermission"
locationListUrl = remoteURL + 'users/api/locationlist'
get_packet_mapped_employees_url = remoteURL + 'packet/api/get_packet_mapped_employees'
apply_employees_packet_mapping_url = remoteURL + 'packet/api/apply_employees_packet_mapping'
leavetypeListUrl = remoteURL + 'leave/api/get_leave_type_list'
apply_packet_rules_url = remoteURL + 'packet/api/apply_packet_rules'
get_packet_leave_rules_url= remoteURL + 'packet/api/get_packet_leave_rules'

# Create your views here.

def packetlist(request):
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
            packetlistreponse = requests.get(packetlistUrl,headers=headers)   
            packetdata = packetlistreponse.json()
            print("packetdata",packetdata)
            return render(request, 'admin/packet/packetmaster/packetlist.html',{'packetlist':packetdata['data']})
        else:
            data = {}
            data['PacketName'] = request.POST.get('PacketName')
            packetaddreponse = requests.post(packetaddUrl,headers=headers,data=data)   
            packetdata = packetaddreponse.json()
            if packetdata['response']['n'] == 1:
                messages.success(request,packetdata['response']['msg'])
                return redirect ('packet:packetlist')
            else:
                messages.error(request,packetdata['response']['msg'])
                return redirect ('packet:packetlist') 
    else:
        return redirect('users:login')
    

def update_packet(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data ={}
    data['id'] = request.POST.get('id')
    data ['PacketName'] = request.POST.get('PacketName')
    print("updatepacketURL",updatepacketURL)
    update_packetResponse = requests.post(updatepacketURL, headers=headers,data=data)
    update_packetData = update_packetResponse.json()
    print("update_packetData",update_packetData)
    if update_packetData['response']['n'] == 1 :
        messages.success(request,update_packetData['response']['msg'])
    else:
        messages.error(request,update_packetData['response']['msg'])
    return HttpResponse(json.dumps(update_packetData), content_type="application/json")


def delete_packet(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data ={}
    data['id'] = request.POST.get('id')
    data ['PacketName'] = request.POST.get('PacketName')
    print("deletepacketURL",deletepacketURL)
    delete_packetResponse = requests.post(deletepacketURL, headers=headers,data=data)
    delete_packetData = delete_packetResponse.json()
    print("delete_packetData",delete_packetData)
    if delete_packetData['response']['n'] == 1 :
        messages.success(request,delete_packetData['response']['msg'])
    else:
        messages.error(request,delete_packetData['response']['msg'])
    return HttpResponse(json.dumps(delete_packetData), content_type="application/json")


def packetmapping(request):
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
            packetlistreponse = requests.get(packetlistUrl,headers=headers)   
            packetdata = packetlistreponse.json()
            location_request = requests.get(locationListUrl,headers=headers)   
            location_response = location_request.json()
            print("location_response",location_response['data'])
            return render(request, 'admin/packet/packetmapping/packetmapping.html',{'packetlist':packetdata['data'],'locations':location_response['data']})
        else:
            data = {}
            data['PacketName'] = request.POST.get('PacketName')
            packetaddreponse = requests.post(packetaddUrl,headers=headers,data=data)   
            packetdata = packetaddreponse.json()
            if packetdata['response']['n'] == 1:
                messages.success(request,packetdata['response']['msg'])
                return redirect ('packet:packetlist')
            else:
                messages.error(request,packetdata['response']['msg'])
                return redirect ('packet:packetlist') 
    else:
        return redirect('users:login')
    




def get_packet_mapped_employees(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data ={}
    data ['PacketId'] = request.POST.get('PacketId')
    data ['Location'] = request.POST.get('Location')
    get_packet_mapped_employees_request = requests.post(get_packet_mapped_employees_url, headers=headers,data=data)
    get_packet_mapped_employees_response = get_packet_mapped_employees_request.json()

    return HttpResponse(json.dumps(get_packet_mapped_employees_response), content_type="application/json")

def apply_employees_packet_mapping(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data =request.POST.copy()

    apply_employees_packet_mapping_request = requests.post(apply_employees_packet_mapping_url, headers=headers,data=data)
    apply_employees_packet_mapping_response = apply_employees_packet_mapping_request.json()

    return HttpResponse(json.dumps(apply_employees_packet_mapping_response), content_type="application/json")


def packetrulebuilder(request):
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
            packetlistreponse = requests.get(packetlistUrl,headers=headers)   
            packetdata = packetlistreponse.json()
            leavetype_request = requests.get(leavetypeListUrl,headers=headers)   
            leavetype_response = leavetype_request.json()
            print("leavetype_response",leavetype_response['data'])
            return render(request, 'admin/packet/packetrulebuilder/packetrulebuilder.html',{'packetlist':packetdata['data'],'leavetypes':leavetype_response['data']})
 
    else:
        return redirect('users:login')
    
def apply_packet_rules(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data =request.POST.copy()

    apply_packet_rules_request = requests.post(apply_packet_rules_url, headers=headers,data=data)
    apply_packet_rules_response = apply_packet_rules_request.json()

    return HttpResponse(json.dumps(apply_packet_rules_response), content_type="application/json")
def get_packet_leave_rules(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data =request.POST.copy()

    get_packet_leave_rules_request = requests.post(get_packet_leave_rules_url, headers=headers,data=data)
    get_packet_leave_rules_response = get_packet_leave_rules_request.json()

    return HttpResponse(json.dumps(get_packet_leave_rules_response), content_type="application/json")






