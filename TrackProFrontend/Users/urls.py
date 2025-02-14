from django.contrib import admin
from django.urls import path, include, re_path
from . import views as v
# from django.conf.urls import url
urlpatterns = [
    path('accessDenied',v.accessDenied, name='accessDenied'),
    path('admin/', admin.site.urls),
    path('home', v.home, name='home'),
    path('admindashboard', v.admindashboard, name='admindashboard'),
    path('dashboard', v.adminhome, name='dashboard'),
    path('get_user_dashboard', v.get_user_dashboard, name='get_user_dashboard'),
    path('', v.loginPage, name='login'),
    path('logout', v.logout, name='logout'),
    path('testhome', v.testhome, name='testhome'),
    path('notificationlist', v.notificationlist, name='notificationlist'),
    path('leavenotificationlist', v.leavenotificationlist, name='leavenotificationlist'),
    path('readnotification', v.readNotification, name='readNotification'),
    path('sendActiveREminderMail', v.sendActiveREminderMail, name='sendActiveREminderMail'),
    path('updatepassword/<int:id>', v.updatepassword, name='updatepassword'),
    path('update/<str:id>', v.update_employee, name='update_employee'),
    path('employeelist', v.employeelist, name='employeelist'),
    path('add', v.addemployee, name='addemployee'),
    path('block_employee/<int:id>', v.block_employee, name='block_employee'),
    path('block_employee_ajax', v.block_employee_ajax, name='block_employee_ajax'),
    
    path('users/role', v.rolelist, name='rolelist'),
    path('location', v.locationlist, name='locationlist'),
    path('delete_location/<int:id>', v.delete_location, name='delete_location'),
    path('updatelocation', v.updateLocation, name='updateLocation'),
    path('designation', v.designationlist, name='designationlist'),
    path('updatedesignation', v.updatedesignation, name='updatedesignation'),
    path('delete_designation/<int:id>', v.delete_designation, name='delete_designation'),
  
    path('department', v.departmentlist, name='departmentlist'),
    path('updatedepartment', v.updatedepartment, name='updatedepartment'),
    path('delete_department/<int:id>', v.delete_department, name='delete_department'),
    path('deleteusermappings', v.deleteusermappings, name='deleteusermappings'),

    path('usermapping', v.addusermanagermapping, name='addusermanagermapping'),
    path('MappingSelectOnchangeAjax', v.MappingSelectOnchangeAjax,
         name='MappingSelectOnchangeAjax'), 
    path('trackpro-report',v.war_report,name="trackpro-report"),
    path('attendance_cal_year_change',v.attendance_cal_year_change , name="attendance_cal_year_change"),
    path('get_leaves_and_latemarks_by_date',v.get_leaves_and_latemarks_by_date , name="get_leaves_and_latemarks_by_date"),
    path('getattendancebydate',v.getattendancebydate , name="getattendancebydate"),
    path('attendance_cal',v.attendance_cal , name="attendance_cal"),
    path('late_attendance',v.late_attendance , name="late_attendance"),
    path('secondary-info',v.secondary_info , name="secondary_info"),
    path('secondary-info-ajax',v.secondary_info_ajax , name="secondary_info_ajax"),
    path('forget-password',v.forgetpassword , name="forgetpassword"),
    path('reset-password/<str:id>',v.reset_password , name="reset_password"),
    path('punch-indata',v.punch_indata , name="punch_indata"),
    path('punch-outdata',v.punch_outdata , name="punch_outdata"),

    path('get-data',v.get_data , name="get_data"),
    path('permission',v.permission , name="permission"),
    path('get_the_user_device_location',v.get_the_user_device_location , name="get_the_user_device_location"),

    #Added attendance
     path('attendance',v.attendance , name="attendance"),
     path('appendfiledata', v.appendfiledata, name="appendfiledata"),
     path('monthlydata', v.monthlydata, name="monthlydata"),

     #added for role permissions
     path('GetRolePermissions',v.GetRolePermissions , name="GetRolePermissions"),
     path('addduplicaterole',v.addduplicaterole , name="addduplicaterole"),
     path('deleterole',v.deleterole , name="deleterole"),
     path('Editrolename',v.Editrolename , name="Editrolename"),
     path('updatemultiplerole',v.updatemultiplerole , name="updatemultiplerole"),

     path('getadminholidaydata',v.getadminholidaydata , name="getadminholidaydata"),
     path('getadminscoredata',v.getadminscoredata , name="getadminscoredata"),
     path('employee_filter',v.employee_filter , name="employee_filter"),
     path ('getcompanypackages',v.getcompanypackages , name="getcompanypackages"),
     path ('getSAincomepoints',v.getSAincomepoints , name="getSAincomepoints"),
     path ('getcompanyleadspoints',v.getcompanyleadspoints , name="getcompanyleadspoints"),
     path ('addapproveactionnotf',v.addapproveactionnotf , name="addapproveactionnotf"),
     path ('addrejectactionnotf',v.addrejectactionnotf , name="addrejectactionnotf"),
     path ('filternotificationslist',v.filternotificationslist , name="filternotificationslist"),
     path('Teamfiltertracker', v.Teamfiltertracker, name="Teamfiltertracker"),
     path('admin_att_overview', v.admin_att_overview, name="admin_att_overview"),
     path('admin_att_list', v.admin_att_list, name="admin_att_list"),
     path('excel_admin_att_list', v.excel_admin_att_list, name="excel_admin_att_list"),
     path('admin_attmodal_data', v.admin_attmodal_data, name="admin_attmodal_data"),
     
     
     path('document-verification/<str:id>', v.document_verification, name="document-verification"),
     
     path('user-secondaryinfo/<str:id>', v.user_secondaryinfo, name="user-secondaryinfo"),
     path('Announcement',v.Announcementlist, name="Announcementlist"),
     path('updateAnnouncement',v.updateAnnouncement, name="updateAnnouncement"),
     path('delete_Announcement/<int:id>',v.delete_Announcement, name="delete_Announcement"),    
     path('lateAttendance',v.lateAttendance, name="lateAttendance"),
     path('excellatemarkreport',v.excellatemarkreport, name="excellatemarkreport"),
     


     
     # ----
     path('onboarding-list', v.onboarding_list, name="onboarding-list"),
     path('onboard-login-password/<int:id>', v.onboard_login_password, name="onboard-login-password"),
     path('thank-u', v.thank_u, name="thank-u"),
     # (remove frm ajax) Frontend 
     path('accept-document', v.accept_document, name="accept-document"),
     path('rejected-Document', v.rejectedDocument, name="rejected-Document"),
     path('updatePersonal-Details-SecondaryInfo', v.updatePersonalDetailsSecondaryInfo, name="updatePersonal-Details-SecondaryInfo"),
     path('update-EmployeDetails-Secondary-Info', v.updateEmployeDetailsSecondaryInfo, name="update-EmployeDetails-Secondary-Info"),
     path('update-Details-And-Document', v.updateDetailsAndDocument, name="update-Details-And-Document"),
     path('add-updatePersonal-Details-Secondary-Info', v.add_updatePersonalDetailsSecondaryInfo, name="add-updatePersonal-Details-Secondary-Info"),
     path('add_educational_qualification_details', v.add_educational_qualification_details, name="add_educational_qualification_details"),
     path('add_user_previous_company', v.add_user_previous_company, name="add_user_previous_company"),
     path('edit_user_previous_company', v.edit_user_previous_company, name="edit_user_previous_company"),
     path('getusercompanydetails', v.getusercompanydetails, name="getusercompanydetails"),
     path('deleteusercompanydetails', v.deleteusercompanydetails, name="deleteusercompanydetails"),
    
    
     path('add-updateEmploye-Details-Secondary-Info', v.add_updateEmployeDetailsSecondaryInfo, name="add-updateEmploye-Details-Secondary-Info"),
     path('add-secondaryInfo-LinkApi', v.add_secondaryInfoLinkApi, name="add-secondaryInfo-LinkApi"),

     path('baseproj_emplist', v.baseproj_emplist, name="baseproj_emplist"),
     path('get_emp_by_id', v.get_emp_by_id, name="get_emp_by_id"),
     path('emplist', v.emplist, name="emplist"),

    #holiday master
     path('holidaylist', v.holidaylist, name="holidaylist"),
     path('Holidays', v.Holidays, name="Holidays"),
     path('updateholidays', v.updateholidays, name="updateholidays"),
     path('delete_holidays', v.delete_holidays, name="delete_holidays"),
     path('getstatesbycountryid', v.getstatesbycountryid, name="getstatesbycountryid"),
     path('getcitiesbystateid', v.getcitiesbystateid, name="getcitiesbystateid"),
     path('searchcities',v.searchcities,name="searchcities"),
     path('searchstatecountry',v.searchstatecountry,name="searchstatecountry"),

     #otp
     path('OTPEmailsent',v.OTPEmailsent,name="OTPEmailsent"),
     path('Updateprofile',v.Updateprofile,name="Updateprofile"),

     path('adminupdate_emp',v.adminupdate_emp,name="adminupdate_emp"),
     path('Attendancerequest',v.Attendancerequest,name="Attendancerequest"),
     path('Attendancerequest_action',v.Attendancerequest_action,name="Attendancerequest_action"),


     path('Employeerequest',v.Employeerequest,name="Employeerequest"),
     path('cancelattendaancerequest',v.cancelattendaancerequest,name="cancelattendaancerequest"),
     path('attendanceupdate',v.attendanceupdate,name="attendanceupdate"),

     
     
    path('send_onboarding_form/<str:id>', v.send_onboarding_form, name='send_onboarding_form'),

    path('get_attendance_mapped_employees',v.get_attendance_mapped_employees,name="get_attendance_mapped_employees"),
    path('update_employee_first_step', v.update_employee_first_step, name="update_employee_first_step"),
    path('update_employee_second_step', v.update_employee_second_step, name="update_employee_second_step"),
    path('update_employee_third_step', v.update_employee_third_step, name="update_employee_third_step"),
    path('update_employee_fourth_step', v.update_employee_fourth_step, name="update_employee_fourth_step"),
    path('update_employee_fifth_step', v.update_employee_fifth_step, name="update_employee_fifth_step"),
    
    path('getrolelist', v.getrolelist, name="getrolelist"),
    path('getdesignationlist', v.getdesignationlist, name="getdesignationlist"),
    path('getlocationlist', v.getlocationlist, name="getlocationlist"),
    path('getdepartmentlist', v.getdepartmentlist, name="getdepartmentlist"),

    path('update_multiple_employee', v.update_multiple_employee, name="update_multiple_employee"),
    path('get_late_count_per_month', v.get_late_count_per_month, name="get_late_count_per_month"),

    path('emplist', v.emplist, name="emplist"),
    path('get_emp_by_id', v.get_emp_by_id, name="get_emp_by_id"),
    
    path('getuserlist', v.getuserlist, name="getuserlist"),
    path('getshiftevents', v.getshiftevents, name="getshiftevents"),




    
    path('shiftmaster', v.shiftmaster, name="shiftmaster"),
    path('add_shift', v.add_shift, name="add_shift"),
    path('delete_shift', v.delete_shift, name="delete_shift"),
    path('get_shift_details', v.get_shift_details, name="get_shift_details"),
    path('update_shift', v.update_shift, name="update_shift"),
    path('shiftcalenderdashboard', v.shiftcalenderdashboard, name="shiftcalenderdashboard"),

    path('empshiftmaster', v.empshiftmaster, name="empshiftmaster"),
    path('add_empshiftdetails', v.add_empshiftdetails, name="add_empshiftdetails"),
    path('delete_empshiftdetails', v.delete_empshiftdetails, name="delete_empshiftdetails"),

    path('shiftallotment', v.shiftallotment, name="shiftallotment"),
    path('add_empshiftallotment', v.add_empshiftallotment, name="add_empshiftallotment"),
    path('delete_empshiftallotment', v.delete_empshiftallotment, name="delete_empshiftallotment"),
    path('bulkuploadshiftallotment', v.bulkuploadshiftallotment, name="bulkuploadshiftallotment"),

    path('employeeshifthistory', v.employeeshifthistory, name="employeeshifthistory"),

    path('get_all_shifts_employees', v.get_all_shifts_employees, name="get_all_shifts_employees"),
    path('get_all_emp_attendance_by_date',v.get_all_emp_attendance_by_date , name="get_all_emp_attendance_by_date"),
    path('get_sift_emp_attendance_by_date',v.get_sift_emp_attendance_by_date , name="get_sift_emp_attendance_by_date"),
    path('get_sift_emp_attendance_and_task_by_date',v.get_sift_emp_attendance_and_task_by_date , name="get_sift_emp_attendance_and_task_by_date"),
    
    path('get_alloted_shift_header_details',v.get_alloted_shift_header_details , name="get_alloted_shift_header_details"),
    path('shift_history_by_month',v.shift_history_by_month , name="shift_history_by_month"),
    path('paginationshiftallotmentlist',v.paginationshiftallotmentlist , name="paginationshiftallotmentlist"),
    path('getcalendershedule',v.getcalendershedule , name="getcalendershedule"),
    path('change_working_status',v.change_working_status , name="change_working_status"),
    path('mark_forced_system_checkout',v.mark_forced_system_checkout , name="mark_forced_system_checkout"),
    
    
    path('updateemployeetype', v.updateemployeetype, name='updateemployeetype'),
    path('employeetypemaster', v.employeetypemaster, name='employeetypemaster'),
    path('delete_employeetype', v.delete_employeetype, name='delete_employeetype'),
    path('getemployeetypelist', v.getemployeetypelist, name='getemployeetypelist'),

    #RuleBuilder
    path('typerules',v.typerules, name='typerules'),
    path('update_employee_type_rules',v.update_employee_type_rules, name='update_employee_type_rules'),
    path('delete_employee_type_rules',v.delete_employee_type_rules, name='delete_employee_type_rules'),
    
    path('attendanceexcelreport', v.attendanceexcelreport, name="attendanceexcelreport"),
    path('shiftexcelreport', v.shiftexcelreport, name="shiftexcelreport"),
    path('getemployeeallotedshift', v.getemployeeallotedshift, name="getemployeeallotedshift"),
    path('swapshift', v.swapshift, name="swapshift"),
    
    path('warningmail', v.warningmail, name="warningmail"),
    path('GetMailHistory', v.GetMailHistory, name="GetMailHistory"),
    path('apply_compoff', v.apply_compoff, name="apply_compoff"),
    path('get_compoffs', v.get_compoffs, name="get_compoffs"),
    path('claim_compoff', v.claim_compoff, name="claim_compoff"),
    path('withdraw_compoff', v.withdraw_compoff, name="withdraw_compoff"),

    path('compoff_requests', v.compoff_requests, name="compoff_requests"),
    path('change_claim_compoff_date', v.change_claim_compoff_date, name="change_claim_compoff_date"),
    
    path('get_compoff_requests', v.get_compoff_requests, name="get_compoff_requests"),
    path('get_applications_requests', v.get_applications_requests, name="get_applications_requests"),

    path('approve_compoff', v.approve_compoff, name="approve_compoff"),
    path('reject_compoff', v.reject_compoff, name="reject_compoff"),
    path('reschedule_compoff', v.reschedule_compoff, name="reschedule_compoff"),

]