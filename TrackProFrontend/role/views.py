from django.shortcuts import render,redirect
from django.contrib import messages
from Users.views import remoteURL
import requests
from django.http.response import HttpResponse,HttpResponseRedirect
import json
from Users.views import accessToPage,accessDenied

rolelistUrl = remoteURL + 'users/api/rolelist'
roleaddUrl = remoteURL + 'users/api/addrole'
roledeleteUrl = remoteURL + 'users/api/delete_role'
updateroleURL = remoteURL + "users/api/updaterole"
menuitemlistURL = remoteURL + "users/api/menuitem"
addPermissionURL = remoteURL + "users/api/addpermission"
getPermissionURL = remoteURL + "users/api/getPermission"
addUserURL = remoteURL + "users/api/adduser"
userListURL = remoteURL + "users/api/userlist"
getUserURL = remoteURL + "users/api/getuser"
updateUserURL = remoteURL + "users/api/userupdate"
# Create your views here.

def rolelsit(request):
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
            rolelistreponse = requests.get(rolelistUrl,headers=headers)   
            roledata = rolelistreponse.json()
            return render(request, 'admin/rolemaster/role.html',{'rolelist':roledata['data']})
        else:
            data = {}
            data['RoleName'] = request.POST.get('RoleName')
            roleaddreponse = requests.post(roleaddUrl,headers=headers,data=data)   
            roledata = roleaddreponse.json()
            if roledata['n'] == 1:
                messages.success(request,roledata['Msg'])
                return redirect ('role:rolelsit')
            else:
                messages.error(request,roledata['Msg'])
                return redirect ('role:rolelsit') 
    else:
        return redirect('users:login')

def updateRole(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data ={}
    roleId = request.POST.get('roleId')
    data ['RoleName'] = request.POST.get('RoleName')
    updateRoleStringUrl = updateroleURL + "?roleID=" + str(roleId)
    updateRoleResponse = requests.post(updateRoleStringUrl, headers=headers,data=data)
    updateRoleData = updateRoleResponse.json()
    if updateRoleData['n'] == 1 :
        messages.success(request,updateRoleData['Msg'])
    else:
        messages.error(request,updateRoleData['Msg'])
    return HttpResponse(json.dumps({'data': updateRoleData}), content_type="application/json")

def getpermission(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data ={}
    roleId = request.POST.get('RoleID')
    getPermissionStr = getPermissionURL + "?RoleID=" + str(roleId)
    getPermissionResponse = requests.get(getPermissionStr, headers=headers)
    getpermissionData = getPermissionResponse.json()
    # if getpermissionData['n'] == 1 :
    #     messages.success(request,updateRoleData['Msg'])
    # else:
    #     messages.error(request,updateRoleData['Msg'])
    return HttpResponse(json.dumps({'data': getpermissionData}), content_type="application/json")

def permission(request):
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
        data = {}
        if request.method == "POST":
            data['RoleID'] = request.POST.get('RoleID')
            data['MenuID'] = request.POST.getlist('check')
            addPermissionReponse = requests.post(addPermissionURL,headers=headers,data=data)   
            permissiondata = addPermissionReponse.json()
            if permissiondata['response']['n'] == 1:
                messages.success(request,permissiondata['response']['msg'])
                return redirect('role:permission')
            else:
                messages.error(request,permissiondata['response']['msg'])
                return redirect('role:permission')
        else:
            rolelistreponse = requests.get(rolelistUrl,headers=headers)   
            roledata = rolelistreponse.json()
            menuitemresponse = requests.get(menuitemlistURL,headers=headers)   
            menuitemdata = menuitemresponse.json()
            return render(request, 'admin/rolemaster/permission.html',{'rolelist':roledata['data'],'Menu':menuitemdata})
        
           
    else:
        return redirect('users:login')


    
def superuserlist(request):
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
            data['Firstname'] = request.POST.get('firstName')
            data['Lastname'] = request.POST.get('lastName')
            data['Password'] = request.POST.get('password')
            data['password'] = request.POST.get('password')
            data['RoleID'] = request.POST.get('role')
            data['Phone'] = request.POST.get('mobileNumber')
            data['email'] = request.POST.get('email')
            adduserreponse = requests.post(addUserURL,headers=headers,data=data)   
            addUserData = adduserreponse.json()
            if addUserData['n'] == 1:
                messages.success(request,addUserData['Msg'])
                return redirect('role:superuserlist')
            else:
                messages.error(request,addUserData['Msg'])
                return redirect('role:superuserlist')
        else:
            rolelistreponse = requests.get(rolelistUrl,headers=headers)   
            roledata = rolelistreponse.json()
            userlistreponse = requests.get(userListURL,headers=headers)   
            userdata = userlistreponse.json()
            return render(request, 'superadmin/usermaster/userlist.html',{'rolelist':roledata['data'],'userlist':userdata['data']})
    else:
        return redirect('users:login')

def updatesuperuser(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.session.get('PasswordChanged') == False:
            return redirect('users:updatepassword', id=request.session.get('userID'))
        data = {}
        if request.method == "GET":
            rolelistreponse = requests.get(rolelistUrl,headers=headers)   
            roledata = rolelistreponse.json()
            getUserStrUrl = getUserURL + "?userID=" + str(id)
            getUserReponse = requests.get(getUserStrUrl,headers=headers)
            getUserData = getUserReponse.json()
            return render(request, 'superadmin/usermaster/updateuser.html',{'rolelist':roledata['data'],'userinfo':getUserData['data']})
        else:
            data['Firstname'] = request.POST.get('firstName')
            data['Lastname'] = request.POST.get('lastName')
            data['RoleID'] = request.POST.get('role')
            data['Phone'] = request.POST.get('mobileNumber')
            data['email'] = request.POST.get('email')
            updateStrUrl = updateUserURL + "?userID=" + str(id)
            updateuserreponse = requests.post(updateStrUrl,headers=headers,data=data)   
            updateUserData = updateuserreponse.json()
            if updateUserData['n'] == 1:
                messages.success(request,updateUserData['Msg'])
                return redirect('role:superuserlist')
            else:
                messages.error(request,updateUserData['Msg'])
                return redirect('role:superuserlist')
    else:
        return redirect('users:login')
        

def delete_role(request,id):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data={}
    data['id']=id
    delete_request = requests.post(roledeleteUrl, headers=headers,data=data)
    delete_response = delete_request.json()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))