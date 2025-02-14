from django.contrib import admin
from django.urls import path, include, re_path
from . import views as v
# from django.conf.urls import url
urlpatterns = [
    path('', v.getcompanylist, name='getcompanylist'),
   
    path('billingPeriodbyid', v.BillingPeriodbyid, name='BillingPeriodbyid'),
    path('update/<int:id>', v.CompanyById, name='CompanyById'),
    path('leads', v.companyleads, name='companyleads'),
    path('payment-history', v.comapanypaymenthistory, name='comapanypaymenthistory'),
    # path('payment', v.makecompanypayment, name='makecompanypayment'),
    path('planlist', v.planlist, name='planlist'),
   
    path('reminder', v.reminder, name='reminder'),
    path('companytype', v.companyType, name='companyType'),
    path('updatecompanytype', v.updateCompanyType, name='updateCompanyType'),
    path('sendreminder', v.sendReminder, name='sendReminder'),
    path('updateplan/<int:id>', v.updatePlan, name='updatePlan'),
    path('viewcompany/<int:id>', v.viewCompany, name='viewCompany'),
    path('company-rule', v.companyrule, name='companyrule'),
    path('updatemasters', v.updatemasters, name='updatemasters'),

  
    path('designation-master-file', v.designationmaster, name='designationmaster'),
    path('departmentfiledata', v.departmentfiledata, name='departmentfiledata'),
    path('locationfiledata', v.locationfiledata, name='locationfiledata'),
    # path('allmasters', v.allMasters, name='allMasters'),
    path('employee-excel',v.addEmployeeExcel,name='addEmployeeExcel'),
    path('addrules',v.addrules , name="addrules"),
    path('updaterules',v.updaterules , name="updaterules"),
    path('leaverule',v.fleaverule , name="fleaverule"),
    path('attrule',v.fattrule , name="fattrule"),
    path('trackprorule',v.ftrackprorule , name="ftrackprorule"),
    path('company_uploadmasters',v.updatemasters , name="updatemasters"),
    path('news',v.news , name="news"),
    path('deleteanouncement/<int:id>',v.deleteanouncement , name="deleteanouncement"),
    path('deletenews/<int:id>',v.deletenews , name="deletenews"),
    # delete company api created
    path('delete_company/<int:id>',v.delete_company , name="delete_company"),
    path('delete_company_type/<int:id>',v.delete_company_type , name="delete_company_type"),
    path('userblock/<int:id>',v.userblock , name="userblock"),
    path('userunblock/<int:id>',v.userunblock , name="userunblock"),

   
]