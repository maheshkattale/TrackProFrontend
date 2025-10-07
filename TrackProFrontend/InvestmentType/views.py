from django.shortcuts import render, redirect, HttpResponse,HttpResponseRedirect
import requests
import os
import json
from helpers.static_info import *
from django.contrib import messages
# Create your views here.

def investmentlist(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            data = {}
            requestdata = request.POST
            data['sectionId']=request.POST.get('sectionId')
            data['Name']=request.POST.get('Name')
            data['Description']=request.POST.get('Description')
            data['Max_limit']=request.POST.get('Max_limit')
            data['ProofRequired']=request.POST.get('ProofRequired')
            data['Exemption_Limit']=request.POST.get('Exemption_Limit')
            data['DocRequired']=request.POST.get('DocRequired')
            data['InvestmentSingleBatch']=request.POST.get('InvestmentSingleBatch')
            data['SortOrder']=request.POST.get('SortOrder')
            data['Invest_TypeCode']=request.POST.get('Invest_TypeCode')
            data['ExemptSection']=request.POST.get('ExemptSection')
            data['No_Projection']=request.POST.get('No_Projection')
            # data['Section']=request.POST.get('Section')
            data['HideOnDeclaration']=request.POST.get('HideOnDeclaration')
            data['NewTaxRegimeApp']=request.POST.get('NewTaxRegimeApp')
            data['LTA_slabApplicable']=request.POST.get('LTA_slabApplicable')
            if 'InvestmentSingleBatch' in requestdata.keys():
                data['InvestmentSingleBatch']= True 
            else:
                data['InvestmentSingleBatch']= False 
            if 'HideOnDeclaration' in requestdata.keys():
                data['HideOnDeclaration']= True
            else:
                data['HideOnDeclaration']= False 
            if 'ProofRequired' in requestdata.keys():
                data['ProofRequired'] = True
            else:
                data['ProofRequired']= False 
            if 'LTA_slabApplicable' in requestdata.keys():
                data['LTA_slabApplicable']= True
            else:
                data['LTA_slabApplicable']= False 
            if 'No_Projection' in requestdata.keys():
                data['No_Projection']= True
            else:
                data['No_Projection']= False 
            if 'status' in requestdata.keys():
                data['Is_Active']= True
            else:
                data['Is_Active']= False 
            addinvestmenttask = requests.post(remoteURL+"Investment/api/InvestmentType", data=data, headers=headers)
            addinvestmenttask_response = addinvestmenttask.json()
            messages.success(request,addinvestmenttask_response['response']['msg'])
            return redirect("InvestmentType:investment-list")
        listInvestmentType_request = requests.get(remoteURL+"Investment/api/typelist",headers=headers)
        listInvestmentType_response = listInvestmentType_request.json()
        
        section_list_request = requests.get(remoteURL+"Investment/api/sectionlist",headers=headers)
        section_list_response = section_list_request.json()
        return render(request,'admin/InvestmentType/investmenttype.html',{'listInvestment':listInvestmentType_response['data'],'section_list':section_list_response['data']})


def updateinvestment(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data ={}
    data['id'] = request.POST.get('id')
    data['sectionId']=request.POST.get('sectionId')
    data['Name']=request.POST.get('Name')
    data['Description']=request.POST.get('Description')
    data['Max_limit']=request.POST.get('Max_limit')
    data['ProofRequired']=request.POST.get('ProofRequired')
    data['Exemption_Limit']=request.POST.get('Exemption_Limit')
    data['DocRequired']=request.POST.get('DocRequired')
    data['InvestmentSingleBatch']=request.POST.get('InvestmentSingleBatch')
    data['SortOrder']=request.POST.get('SortOrder')
    data['Invest_TypeCode']=request.POST.get('Invest_TypeCode')
    data['ExemptSection']=request.POST.get('ExemptSection')
    data['No_Projection']=request.POST.get('No_Projection')
    # data['Section']=request.POST.get('Section')
    data['HideOnDeclaration']=request.POST.get('HideOnDeclaration')
    data['NewTaxRegimeApp']=request.POST.get('NewTaxRegimeApp')
    data['LTA_slabApplicable']=request.POST.get('LTA_slabApplicable')
    data['Is_Active']=request.POST.get('status')
    updateinvestResponse = requests.post(remoteURL+"Investment/api/typeupdate", headers=headers,data=data)
    updateinvestData = updateinvestResponse.json()
    if updateinvestData['response']['n'] == 1 :
        messages.success(request,updateinvestData['response']['msg'])
    else:
        messages.error(request,updateinvestData['response']['msg'])
    return HttpResponse(json.dumps({'data': updateinvestData}), content_type="application/json")

def deleteinvestment(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['id']=id
        InvtypedeleteAPI_request = requests.post(remoteURL+"Investment/api/typedelete", headers=headers,data=data)
        InvtypedeleteAPI_response = InvtypedeleteAPI_request.json()
        
        messages.success(request,InvtypedeleteAPI_response['response']['msg'])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('users:login')
    

def sectionlist(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            data = {}
            data['Name']=request.POST.get('Name')
            data['Description']=request.POST.get('Description')
            data['Tentative_limits']=request.POST.get('Tentativelimit')
            data['Is_Active'] = request.POST.get('status')
            addsectiontask = requests.post(
                remoteURL+"Investment/api/section", data=data, headers=headers)
            addsectiontask_response = addsectiontask.json()
            messages.success(request,addsectiontask_response['response']['msg'])
            return redirect("InvestmentType:section")
    section_list_request = requests.get(remoteURL+"Investment/api/sectionlist",headers=headers)
    section_list_response = section_list_request.json()
    return render(request,'admin/InvestmentType/section.html',{'section_list':section_list_response['data']})


def updatesection(request):
    tok = request.session.get('token', False)
    t = 'Token {}'.format(tok)
    headers = {'Authorization': t}
    data ={}
    data['id'] = request.POST.get('sectionId')
    data['Name']=request.POST.get('Name')
    data['Description']=request.POST.get('Description')
    data['Tentative_limits']=request.POST.get('Tentativelimit')
    data['Is_Active'] = request.POST.get('status')
    updateDeptResponse = requests.post(remoteURL+"Investment/api/sectionupdate", headers=headers,data=data)
    updateDeptData = updateDeptResponse.json()
    if updateDeptData['response']['n'] == 1 :
        messages.success(request,updateDeptData['response']['msg'])
    else:
        messages.error(request,updateDeptData['response']['msg'])
    return HttpResponse(json.dumps({'data': updateDeptData}), content_type="application/json")



def deletesection(request,id):
    tok = request.session.get('token', False)
    if tok:
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        data={}
        data['id']=id
        sectiondeleteAPI_request = requests.post(remoteURL+"Investment/api/sectiondelete", headers=headers,data=data)
        sectiondeleteAPI_response = sectiondeleteAPI_request.json()
        
        messages.success(request,sectiondeleteAPI_response['response']['msg'])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('users:login')
    
    
    
def configurationlist(request):
    tok = request.session.get('token', False)
    if tok:
        tok = request.session['token']
        t = 'Token {}'.format(tok)
        headers = {'Authorization': t}
        if request.method == 'POST':
            data = {}
            data['Name']=request.POST.get('Name')
            data['Description']=request.POST.get('Description')
            data['Tentative_limits']=request.POST.get('Tentativelimit')
            data['Is_Active'] = request.POST.get('status')
            addsectiontask = requests.post(
                remoteURL+"Investment/api/section", data=data, headers=headers)
            addsectiontask_response = addsectiontask.json()
            messages.success(request,addsectiontask_response['response']['msg'])
            return redirect("InvestmentType:section")
    section_list_request = requests.get(remoteURL+"Investment/api/sectionlist",headers=headers)
    section_list_response = section_list_request.json()
    return render(request,'admin/InvestmentType/section.html',{'section_list':section_list_response['data']})