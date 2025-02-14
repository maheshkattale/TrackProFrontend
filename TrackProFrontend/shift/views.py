from django.shortcuts import render,redirect
from django.contrib import messages
from Users.views import remoteURL
import requests
from django.http.response import HttpResponse,HttpResponseRedirect
import json
from Users.views import accessToPage,accessDenied

rolelistUrl = remoteURL + 'users/api/rolelist'
# Create your views here.

def shift_swap_requests(request):
    tok = request.session.get('token', False)
    if tok:
        return render(request, 'admin/shiftmaster/shift_swap_requests.html')
    else:
        return redirect('users:login')
    
def get_shift_swap_applications(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data=request.POST.copy()
            status=request.POST.get('status')
            get_applications_url = remoteURL+'Shift/api/get_manager_'+status+'_shift_swap_applications'
            get_applications_request = requests.post(get_applications_url,data=data,headers=headers)
            get_applications_response = get_applications_request.json()
            return HttpResponse(json.dumps(get_applications_response),content_type='application/json')
    else:
        return redirect('users:login')

def approve_application(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data=request.POST.copy()
            approve_applications_url = remoteURL+'Shift/api/approve_shift_swap_applications'
            approve_applications_request = requests.post(approve_applications_url,data=data,headers=headers)
            approve_applications_response = approve_applications_request.json()
            return HttpResponse(json.dumps(approve_applications_response),content_type='application/json')
    else:
        return redirect('users:login')
    
def reject_application(request):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == "POST":
            data=request.POST.copy()
            reject_applications_url = remoteURL+'Shift/api/reject_shift_swap_applications'
            reject_applications_request = requests.post(reject_applications_url,data=data,headers=headers)
            reject_applications_response = reject_applications_request.json()
            return HttpResponse(json.dumps(reject_applications_response),content_type='application/json')
    else:
        return redirect('users:login')







